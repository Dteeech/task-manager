# views/widgets/task_row_widget.py
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QComboBox
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QIcon, QColor

class TaskRowWidget(QWidget):
    """Widget pour l'affichage d'une tâche en mode liste."""
    edit_clicked = Signal(int)
    delete_clicked = Signal(int)
    status_changed = Signal(int, str)  # id, nouveau statut
    def __init__(self, task: dict):
        super().__init__()
        self.task = task

        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 2, 5, 2)

        # Label du titre
        label = QLabel(f"{task['title']}")
        label.setStyleSheet("font-size: 14px;")
        layout.addWidget(label, alignment=Qt.AlignLeft)
   
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
        self.setStyleSheet("""
            QWidget {
                background-color: white;
                border-bottom: 1px solid #eee;
            }
            QWidget:hover {
                background-color: #fafafa;
            }
        """)

          # === Style global ===
        self.setStyleSheet("""
            QWidget {
                background-color: white;
                border-bottom: 1px solid #eee;
            }
            QComboBox {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 2px 6px;
                background: #fafafa;
            }
            QComboBox:hover {
                background: #f0f0f0;
            }
            QPushButton {
                border: none;
                background: transparent;
            }
            QPushButton:hover {
                background: #f7f7f7;
                border-radius: 5px;
            }
        """)