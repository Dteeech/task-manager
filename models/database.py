# models/database.py
import sqlite3
from pathlib import Path


class DatabaseManager:
    """
    Classe responsable de la connexion SQLite et de l'initialisation des tables.
    """

    def __init__(self, db_path: str = "app_data.db"):
        self.db_path = Path(db_path)
        self.connection = None
        self.connect()
        self._create_tables()

    def connect(self):
        """Établit la connexion à la base SQLite."""
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row  # permet un accès par nom de colonne

    def _create_tables(self):
        """Crée les tables principales si elles n'existent pas."""
        cursor = self.connection.cursor()

        # Table des tâches
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT DEFAULT 'À faire' CHECK(status IN ('À faire', 'En cours', 'Terminée')),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        )

        # Table des commentaires
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id INTEGER NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE
            )
        """
        )

        self.connection.commit()

    def execute(self, query: str, params: tuple = (), fetchone=False, fetchall=False):
        """Exécute une requête SQL avec gestion automatique du commit."""
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()

        if fetchone:
            return cursor.fetchone()
        elif fetchall:
            return cursor.fetchall()
        return None

    def close(self):
        """Ferme proprement la connexion."""
        if self.connection:
            self.connection.close()
