# controllers/task_controller.py
from models.task_model import TaskModel
from PySide6.QtWidgets import QMessageBox
from views.task_detail_view import TaskDetailView

class TaskController:
    def __init__(self, view):
        self.view = view
        self.model = TaskModel()
         
        # Établit la relation entre la vue et son contrôleur
        self.view.parent_controller = self
        # Connecte les signaux de la vue aux méthodes du contrôleur
        self.view.add_button.clicked.connect(self.create_task)

        # Charge les tâches au démarrage
        self.load_tasks()
        
    def load_tasks(self):
        """Charge toutes les tâches depuis la BDD et les affiche via la vue."""
        self.view.clear_tasks()  # Vide la liste avant rechargement

        tasks = self.model.get_all_tasks()
        for task in tasks:
            self.view.add_task_to_list(task)  # affichage via widget custom

    def create_task(self):
        """Crée une nouvelle tâche en base, puis rafraîchit la vue."""
        title, desc = self.view.get_task_inputs()

        if not title:
            self.view.show_error("Veuillez entrer un titre de tâche.")
            return

        try:
            # Crée la tâche dans la base de données
            new_task = self.model.create_task(title, desc)
            print(f"Tâche créée en base : {new_task}")

            # Met à jour l'affichage avec la nouvelle tâche
            self.view.add_task_to_list(new_task)
            self.view.clear_inputs()

        except Exception as e:
            self.view.show_error(f"Erreur lors de la création : {e}")

    def delete_task(self, task_id):
        confirm = QMessageBox.question(
            self.view, "Supprimer", "Supprimer cette tâche ?", 
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm == QMessageBox.Yes:
            self.model.delete_task(task_id)
            self.load_tasks()
    
    # Gestion de la vue détaillée d'une tâche

   
    def open_task_detail(self, task_id):
        """Ouvre la vue de détail d'une tâche dans le QStackedWidget."""
        task = self.model.get_task(task_id)
        if not task:
            self.view.show_error("Tâche introuvable.")
            return

        # Crée la vue de détail (avec parent = stack pour s'assurer d'une hiérarchie Qt correcte)
        detail_view = TaskDetailView(task, parent=self.view.stack, parent_controller=self)

        # Connecte les signaux
        detail_view.back_clicked.connect(self.back_to_main)
        detail_view.status_changed.connect(lambda s: self.update_task_status(task_id, s))
        detail_view.save_clicked.connect(self.update_task)

        # Ajoute et affiche la vue détail dans le stack avec protection contre les erreurs
        try:
            # Vérifie que le widget n'est pas déjà présent avant de l'ajouter
            if self.view.stack.indexOf(detail_view) == -1:
                self.view.stack.addWidget(detail_view)
            self.view.stack.setCurrentWidget(detail_view)
            # Conserve la référence pour un accès ultérieur si nécessaire
            self.detail_view = detail_view
        except RuntimeError:
            # Gestion d'erreur si l'objet C++ du parent a été détruit
            try:
                self.view.show_error("Erreur interne : l'interface a été détruite. Veuillez relancer l'application.")
            except Exception:
                pass


    def back_to_main(self):
        """Retourne à la page principale sans recréer la vue."""
        self.view.stack.setCurrentIndex(0)
        self.load_tasks()

    # Mise à jour du statut depuis la liste principale
    def update_task_status(self, task_id: int, new_status: str):
        self.model.update_status(task_id, new_status)
        # Pas de rechargement complet nécessaire, la mise à jour est instantanée

    def update_task(self, task):
        """Délègue la mise à jour au modèle et retourne à la liste."""
        try:
            self.model.update_task_details(task)
            # Retour à la page principale après la sauvegarde
            self.back_to_main()
        except Exception as e:
            self.view.show_error(f"Erreur lors de la mise à jour : {e}")

    def handle_image_upload(self, task):
        """Gère la mise à jour de l'image d'une tâche."""
        try:
            # Met à jour le chemin de l'image dans la tâche
            self.model.update_task_details(task)
            print(f"Image mise à jour pour la tâche {task['id']}")
        except Exception as e:
            print(f"Erreur lors de la mise à jour de l'image: {e}")
            self.view.show_error(f"Erreur lors de la mise à jour de l'image: {e}")
