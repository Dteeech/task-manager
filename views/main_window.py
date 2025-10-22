# views/main_window.py
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QListWidget, QPushButton, QLineEdit, QLabel, QMessageBox, QListWidgetItem
)
from PySide6.QtCore import Qt
from views.widgets.task_row_widget import TaskRowWidget

class MainWindow(QMainWindow):
    """Vue principale de l'application de gestion de tâches."""

    def __init__(self):
        super().__init__()

        self.parent_controller = None  
        
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

   
    def get_task_inputs(self):
        return self.task_title.text().strip(), self.task_desc.text().strip()

    def clear_inputs(self):
        self.task_title.clear()
        self.task_desc.clear()

    def clear_tasks(self):
        self.task_list.clear()

    def add_task_to_list(self, task: dict):
        """
        Ajoute une tâche dans la liste sous forme de widget personnalisé.
        """
        # 1️⃣ Crée un "slot" (ligne vide) dans la QListWidget
        item = QListWidgetItem()

        # 2️⃣ Crée ton widget custom (TaskRowWidget) en lui passant les données de la tâche
        widget = TaskRowWidget(task)

        # 3️⃣ Ajuste la hauteur de la ligne à la taille du widget
        item.setSizeHint(widget.sizeHint())

        # 4️⃣ Ajoute la ligne vide dans la QListWidget
        self.task_list.addItem(item)

        # 5️⃣ Place le widget à l’intérieur de cette ligne
        self.task_list.setItemWidget(item, widget)

        # 6️⃣ Connecte les signaux du widget à ton contrôleur
        widget.edit_clicked.connect(lambda id=task["id"]: self.parent_controller.edit_task(id))
        widget.delete_clicked.connect(lambda id=task["id"]: self.parent_controller.delete_task(id))

    
        def show_error(self, message: str):
            QMessageBox.warning(self, "Erreur", message)
