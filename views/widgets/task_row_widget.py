# views/widgets/task_row_widget.py
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
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

        # Bouton édition ✏️
        edit_btn = QPushButton()
        edit_btn.setIcon(QIcon.fromTheme("document-edit"))
        edit_btn.setFixedSize(24, 24)
        edit_btn.setStyleSheet("border: none;")
        edit_btn.clicked.connect(lambda: self.edit_clicked.emit(task["id"]))
        layout.addWidget(edit_btn)

        # Bouton suppression 🗑️
        delete_btn = QPushButton()
        delete_btn.setIcon(QIcon.fromTheme("edit-delete"))
        delete_btn.setFixedSize(24, 24)
        delete_btn.setStyleSheet("border: none;")
        delete_btn.clicked.connect(lambda: self.delete_clicked.emit(task["id"]))
        layout.addWidget(delete_btn, alignment=Qt.AlignRight)
