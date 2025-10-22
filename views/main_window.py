# views/main_window.py
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QListWidget, QPushButton, QLineEdit, QLabel, QMessageBox
)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    """Vue principale de l'application de gestion de tâches."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestionnaire de tâches")
        self.setMinimumSize(600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # --- UI ---
        title_label = QLabel("🗂️ Mes Tâches")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 10px;")
        self.layout.addWidget(title_label)

        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        input_layout = QHBoxLayout()
        self.task_title = QLineEdit()
        self.task_title.setPlaceholderText("Titre")
        self.task_desc = QLineEdit()
        self.task_desc.setPlaceholderText("Description...")
        self.add_button = QPushButton("Ajouter")

        input_layout.addWidget(self.task_title)
        input_layout.addWidget(self.task_desc)
        input_layout.addWidget(self.add_button)
        self.layout.addLayout(input_layout)

    # --- Méthodes d’accès aux données ---

    def get_task_inputs(self):
        return self.task_title.text().strip(), self.task_desc.text().strip()

    def clear_inputs(self):
        self.task_title.clear()
        self.task_desc.clear()

    def clear_tasks(self):
        self.task_list.clear()

    def add_task_to_list(self, task: dict):
        self.task_list.addItem(f"{task['id']} - {task['title']} ({task['status']})")

    def show_error(self, message: str):
        QMessageBox.warning(self, "Erreur", message)
