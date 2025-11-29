# views/widgets/task_row_widget.py
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QComboBox
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QIcon, QColor

class TaskRowWidget(QWidget):
    """Widget pour l'affichage d'une tâche en mode liste."""
    edit_clicked = Signal(int)
    delete_clicked = Signal(int)
    status_changed = Signal(int, str)  # id, nouveau statut
    def __init__(self, task: dict, dark_mode=False):
        super().__init__()
        self.task = task
        self.dark_mode = dark_mode

        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 2, 5, 2)

        # Label du titre
        self.title_label = QLabel(f"{task['title']}")
        self.title_label.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.title_label, alignment=Qt.AlignLeft)
   
        # === Statut modifiable (combo coloré) ===
        self.status_colors = {
            "À faire": "#ffb347",
            "En cours": "#6fa3ef",
            "Terminée": "#77dd77"
        }
        self.status_box = QComboBox()
        for status, color in self.status_colors.items():
            self.status_box.addItem(status)
            index = self.status_box.findText(status)
            self.status_box.setItemData(index, QColor(color), Qt.BackgroundRole)

        self.status_box.setCurrentText(task["status"])
        self.status_box.currentTextChanged.connect(
            lambda s: self.status_changed.emit(task["id"], s)
        )
        layout.addWidget(self.status_box, alignment=Qt.AlignRight)

        layout.addStretch()

        # Bouton édition ✏️
        edit_btn = QPushButton()
        edit_btn.setIcon(QIcon("assets/icons/pen.svg"))
        edit_btn.setToolTip("Modifier la tâche")
        edit_btn.setFixedSize(28, 28)
        edit_btn.setCursor(Qt.PointingHandCursor)
        edit_btn.setStyleSheet("""
            QPushButton {
                background-color: #f1f3f5;
                border: 1px solid #d0d0d0;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #e6e9ec;
            }
        """)
        
        edit_btn.clicked.connect(lambda: self.edit_clicked.emit(self.task["id"]))
        
        layout.addWidget(edit_btn, alignment=Qt.AlignRight)

        # Bouton suppression 🗑️
        delete_btn = QPushButton()
        delete_btn.setIcon(QIcon("assets/icons/trash.svg"))
        delete_btn.setToolTip("Supprimer la tâche")
        delete_btn.setFixedSize(28, 28)
        delete_btn.setCursor(Qt.PointingHandCursor)
        delete_btn.setStyleSheet("""
            QPushButton {
                background-color: #ffe3e3;
                border: 1px solid #ffbdbd;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #ffcccc;
            }
        """)
        delete_btn.clicked.connect(lambda: self.delete_clicked.emit(self.task["id"]))
        layout.addWidget(delete_btn, alignment=Qt.AlignRight)
         
        # Layout adaptable
        layout.setAlignment(Qt.AlignVCenter)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        # Stocker les boutons pour le thème
        self.edit_btn = edit_btn
        self.delete_btn = delete_btn
        
        # Appliquer le thème initial
        self.apply_theme(self.dark_mode)
    
    def apply_theme(self, dark_mode):
        """Applique le thème au widget de tâche."""
        self.dark_mode = dark_mode
        if dark_mode:
            self.setStyleSheet(self.get_dark_stylesheet())
        else:
            self.setStyleSheet(self.get_light_stylesheet())
    
    def get_light_stylesheet(self):
        """Style pour le mode clair."""
        return """
            QWidget {
                background-color: white;
                border-bottom: 1px solid #eee;
            }
            QWidget:hover {
                background-color: #fafafa;
            }
            QLabel {
                color: #000000;
            }
            QComboBox {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 2px 6px;
                background: #fafafa;
                color: #000000;
            }
            QComboBox:hover {
                background: #f0f0f0;
            }
            QPushButton {
                background-color: #f1f3f5;
                border: 1px solid #d0d0d0;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #e6e9ec;
            }
        """
    
    def get_dark_stylesheet(self):
        """Style pour le mode sombre."""
        return """
            QWidget {
                background-color: #2d2d2d;
                border-bottom: 1px solid #3d3d3d;
            }
            QWidget:hover {
                background-color: #3d3d3d;
            }
            QLabel {
                color: #e0e0e0;
            }
            QComboBox {
                border: 1px solid #4d4d4d;
                border-radius: 5px;
                padding: 2px 6px;
                background: #3d3d3d;
                color: #e0e0e0;
            }
            QComboBox:hover {
                background: #4d4d4d;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox QAbstractItemView {
                background-color: #2d2d2d;
                color: #e0e0e0;
                selection-background-color: #4d4d4d;
            }
            QPushButton {
                background-color: #3d3d3d;
                border: 1px solid #4d4d4d;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #4d4d4d;
            }
        """