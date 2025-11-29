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
    task_update_failed = Signal(int, str) 

    

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
   
    def get_task(self, task_id: int):
        """Récupère une tâche par son ID."""
        query = "SELECT id, title, description, status FROM tasks WHERE id = ?"

        row = self.db.execute(query, (task_id,), fetchone=True)
        if row:
            return {
                "id": row[0],
                "title": row[1],
                "description": row[2],
                "status": row[3],
                "image_path": row[4] if len(row) > 4 else None
            }
        return None
    
   
    def delete_task(self, task_id: int):
        """Supprime une tâche et émet un signal."""
        self.db.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        self.task_deleted.emit(task_id)

    def update_task_details(self, task):
        try:
            fields = ["title", "description", "status"]
            params = [task.get(field) for field in fields]

            if "image_path" in task:
                fields.append("image_path")
                params.append(task["image_path"])

            set_clause = ", ".join([f"{field} = ?" for field in fields])
            query = f"UPDATE tasks SET {set_clause} WHERE id = ?"
            params.append(task["id"])

            self.db.execute(query, params)
            self.task_updated.emit(task)  # Succès → notifie les vues

        except sqlite3.Error as e:
            print(f"❌ Erreur SQL : {e}")
            self.task_update_failed.emit(task["id"], str(e))  # Échec → notifie l'erreur



    def update_status(self, task_id, status):
        self.db.execute("UPDATE tasks SET status=? WHERE id=?", (status, task_id))


