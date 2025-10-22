# views/widgets/task_row_widget.py
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QSizePolicy
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QIcon

class TaskRowWidget(QWidget):
    """Widget pour l'affichage d'une tâche en mode liste."""
    edit_clicked = Signal(int)
    delete_clicked = Signal(int)

    def __init__(self, task: dict):
        super().__init__()
        self.task = task

        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 2, 5, 2)

        # Label du titre
        label = QLabel(f"{task['title']}  –  {task['status']}")
        label.setStyleSheet("font-size: 14px;")
        layout.addWidget(label, alignment=Qt.AlignLeft)
   
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