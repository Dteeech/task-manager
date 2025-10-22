# controllers/task_controller.py
from models.task_model import TaskModel

class TaskController:
    def __init__(self, view):
        self.view = view
        self.model = TaskModel()

        # Connecte les signaux
        self.view.add_button.clicked.connect(self.create_task)

        # Charge les tâches au démarrage
        self.load_tasks()

    def load_tasks(self):
        """Charge toutes les tâches depuis la base."""
        self.view.clear_tasks()
        for task in self.model.get_all_tasks():
            self.view.add_task_to_list(task)
        

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

