# views/main_window.py
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QListWidget, QPushButton, QLineEdit, QLabel, QMessageBox, QListWidgetItem, QStackedWidget
)
from PySide6.QtCore import Qt, QSettings
from PySide6.QtGui import QIcon
from views.widgets.task_row_widget import TaskRowWidget

class MainWindow(QMainWindow):
    """Vue principale de l'application de gestion de tâches."""

    def __init__(self):
        super().__init__()

        self.parent_controller = None
        self.settings = QSettings("TaskManager", "DarkMode")
        self.dark_mode = self.settings.value("dark_mode", False, type=bool)
        
        # === Stack principal ===
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # === Page principale ===
        self.page_main = QWidget()
        self.layout_main = QVBoxLayout(self.page_main)

       

        self.setWindowTitle("Gestionnaire de tâches")
        self.setMinimumSize(600, 400)

        # Le QStackedWidget est le central widget — on n'écrase pas le central widget
        # Utilise la layout de la page principale créée plus haut
        self.layout = self.layout_main

        # --- Header avec titre et bouton dark mode ---
        header_layout = QHBoxLayout()
        
        self.title_label = QLabel("🗂️ Mes Tâches")
        self.title_label.setAlignment(Qt.AlignCenter)
        header_layout.addStretch()
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()
        
        # Bouton dark mode
        self.dark_mode_btn = QPushButton()
        self.dark_mode_btn.setFixedSize(80, 40)
        self.dark_mode_btn.setCursor(Qt.PointingHandCursor)
        self.dark_mode_btn.setToolTip("Basculer le mode sombre")
        self.dark_mode_btn.clicked.connect(self.toggle_dark_mode)
        self.update_dark_mode_button()
        header_layout.addWidget(self.dark_mode_btn)
        
        self.layout.addLayout(header_layout)

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

        self.stack.addWidget(self.page_main)  # index 0

        self.setWindowTitle("Gestionnaire de tâches")
        self.setMinimumSize(700, 450)
        
        # Appliquer le thème initial
        self.apply_theme()
        
   
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
        widget = TaskRowWidget(task, self.dark_mode)

        # 3️⃣ Ajuste la hauteur de la ligne à la taille du widget
        item.setSizeHint(widget.sizeHint())

        # 4️⃣ Ajoute la ligne vide dans la QListWidget
        self.task_list.addItem(item)

        # 5️⃣ Place le widget à l’intérieur de cette ligne
        self.task_list.setItemWidget(item, widget)

        # 6️⃣ Connecte les signaux du widget à ton contrôleur
        widget.edit_clicked.connect(lambda id=task["id"]: self.parent_controller.open_task_detail(id))
        
        widget.delete_clicked.connect(lambda id=task["id"]: self.parent_controller.delete_task(id))


    def show_error(self, message: str):
        """Affiche une boîte de dialogue d'erreur."""
        QMessageBox.warning(self, "Erreur", message)
    
    def toggle_dark_mode(self):
        """Bascule entre le mode clair et le mode sombre."""
        self.dark_mode = not self.dark_mode
        self.settings.setValue("dark_mode", self.dark_mode)
        self.apply_theme()
        self.update_dark_mode_button()
        
        # Mettre à jour tous les widgets de tâches existants
        for i in range(self.task_list.count()):
            item = self.task_list.item(i)
            widget = self.task_list.itemWidget(item)
            if isinstance(widget, TaskRowWidget):
                widget.apply_theme(self.dark_mode)
    
    def update_dark_mode_button(self):
        """Met à jour l'icône du bouton dark mode."""
        if self.dark_mode:
            self.dark_mode_btn.setText("☀️")
            self.dark_mode_btn.setToolTip("Mode clair")
        else:
            self.dark_mode_btn.setText("🌙")
            self.dark_mode_btn.setToolTip("Mode sombre")
    
    def apply_theme(self):
        """Applique le thème (clair ou sombre) à l'application."""
        if self.dark_mode:
            self.setStyleSheet(self.get_dark_stylesheet())
        else:
            self.setStyleSheet(self.get_light_stylesheet())
    
    def get_light_stylesheet(self):
        """Retourne la feuille de style pour le mode clair."""
        return """
            QMainWindow, QWidget {
                background-color: #ffffff;
                color: #000000;
            }
            QLabel {
                color: #000000;
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            QListWidget {
                background-color: #ffffff;
                border: 1px solid #e0e0e0;
                border-radius: 5px;
            }
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 8px;
            }
            QPushButton {
                background-color: #f5f5f5;
                color: #000000;
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e9e9e9;
            }
            QPushButton#dark_mode_btn {
                background-color: transparent;
                border: none;
                font-size: 24px;
            }
        """
    
    def get_dark_stylesheet(self):
        """Retourne la feuille de style pour le mode sombre."""
        return """
            QMainWindow, QWidget {
                background-color: #1e1e1e;
                color: #e0e0e0;
            }
            QLabel {
                color: #e0e0e0;
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            QListWidget {
                background-color: #2d2d2d;
                border: 1px solid #3d3d3d;
                border-radius: 5px;
                color: #e0e0e0;
            }
            QLineEdit {
                background-color: #2d2d2d;
                color: #e0e0e0;
                border: 1px solid #3d3d3d;
                border-radius: 5px;
                padding: 8px;
            }
            QPushButton {
                background-color: #3d3d3d;
                color: #e0e0e0;
                border: 1px solid #4d4d4d;
                border-radius: 5px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #4d4d4d;
            }
            QPushButton#dark_mode_btn {
                background-color: transparent;
                border: none;
                font-size: 24px;
            }
        """
