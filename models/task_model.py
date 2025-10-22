# models/task_model.py
from PySide6.QtCore import QObject, Signal
from models.database import DatabaseManager


class TaskModel(QObject):
    """
    Modèle métier des tâches.
    Gère la persistance via DatabaseManager et émet des signaux quand les données changent.
    """

    task_added = Signal(dict)
    task_updated = Signal(dict)
    task_deleted = Signal(int)

    def __init__(self, db_path="app_data.db"):
        super().__init__()
        self.db = DatabaseManager(db_path)

    # --- CRUD ---

    def create_task(self, title: str, description: str = "", status: str = "À faire"):
        """Crée une nouvelle tâche et émet un signal."""
        self.db.execute(
            "INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)",
            (title, description, status),
        )
        new_task = self.db.execute(
            "SELECT * FROM tasks ORDER BY id DESC LIMIT 1", fetchone=True
        )
        if new_task:
            task_data = dict(new_task)
            self.task_added.emit(task_data)
            return task_data

    def get_all_tasks(self):
        """Retourne la liste complète des tâches."""
        rows = self.db.execute(
            "SELECT * FROM tasks ORDER BY created_at DESC", fetchall=True
        )
        return [dict(row) for row in rows]

    def get_task_by_id(self, task_id: int):
        """Récupère une tâche par son ID."""
        row = self.db.execute(
            "SELECT * FROM tasks WHERE id=?", (task_id,), fetchone=True
        )
        return dict(row) if row else None

    def update_task(self, task_id: int, title: str, description: str, status: str):
        """Met à jour une tâche et émet un signal."""
        self.db.execute(
            """
            UPDATE tasks 
            SET title=?, description=?, status=?, updated_at=CURRENT_TIMESTAMP
            WHERE id=?
            """,
            (title, description, status, task_id),
        )
        updated = self.get_task_by_id(task_id)
        if updated:
            self.task_updated.emit(updated)
            return updated

    def delete_task(self, task_id: int):
        """Supprime une tâche et émet un signal."""
        self.db.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        self.task_deleted.emit(task_id)
