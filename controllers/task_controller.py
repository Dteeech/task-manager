# controllers/task_controller.py
from models.task_model import TaskModel
from PySide6.QtWidgets import QMessageBox
from views.task_detail_view import TaskDetailView

class TaskController:
    def __init__(self, view):
        self.view = view
        self.model = TaskModel()
         
         #On dit à la Vue : “Voici ton contrôleur parent”
        self.view.parent_controller = self
        # Connecte les signaux
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
            # 🔹 Appel au modèle (écriture en BDD)
            new_task = self.model.create_task(title, desc)
            print(f"Tâche créée en base : {new_task}")

            # 🔹 Rafraîchit la vue avec la réponse réelle du modèle
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
    
     # --- Modification via la vue détail ---

   
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

        # Ajoute et affiche la page détail dans le stack en protégeant l'appel
        try:
            # addWidget lèvera si le widget C++ parent a été détruit
            if self.view.stack.indexOf(detail_view) == -1:
                self.view.stack.addWidget(detail_view)
            self.view.stack.setCurrentWidget(detail_view)
            # conserve la référence si besoin
            self.detail_view = detail_view
        except RuntimeError:
            # Si la stack a été détruite côté C++ -> affiche message et tente une récupération minimale
            try:
                self.view.show_error("Erreur interne : l'interface a été détruite. Veuillez relancer l'application.")
            except Exception:
                pass


    def back_to_main(self):
        """Retourne à la page principale sans recréer la vue."""
        self.view.stack.setCurrentIndex(0)
        self.load_tasks()

    # --- Update status depuis liste principale ---
    def update_task_status(self, task_id: int, new_status: str):
        self.model.update_status(task_id, new_status)
    # Optionnel : pas besoin de reload complet si tu veux instantané
    # self.load_tasks()

    def update_task(self, task):
        """Délègue la mise à jour au modèle."""
        self.model.update_task_details(task)

    def handle_image_upload(self, task):
        """Gère la mise à jour de l'image d'une tâche."""
        try:
            # Met à jour le chemin de l'image dans la tâche
            self.model.update_task_details(task)
            print(f"Image mise à jour pour la tâche {task['id']}")
        except Exception as e:
            print(f"Erreur lors de la mise à jour de l'image: {e}")
            self.view.show_error(f"Erreur lors de la mise à jour de l'image: {e}")
