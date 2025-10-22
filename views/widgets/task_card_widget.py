# views/widgets/task_card_widget.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QIcon

class TaskCardWidget(QWidget):
    """Widget pour l'affichage d'une tâche en mode carte (kanban)."""
    edit_clicked = Signal(int)
    delete_clicked = Signal(int)

    def __init__(self, task: dict):
        super().__init__()
        self.task = task

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)

        # Titre de la tâche
        title = QLabel(task["title"])
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)

        # Description
        if task.get("description"):
            desc = QLabel(task["description"])
            desc.setWordWrap(True)
            layout.addWidget(desc)

        # Ligne boutons
        btn_layout = QHBoxLayout()
        edit_btn = QPushButton()
        edit_btn.setIcon(QIcon.fromTheme("document-edit"))
        edit_btn.setFixedSize(24, 24)
        edit_btn.setStyleSheet("border: none;")
        edit_btn.clicked.connect(lambda: self.edit_clicked.emit(task["id"]))
        btn_layout.addWidget(edit_btn)

        delete_btn = QPushButton()
        delete_btn.setIcon(QIcon.fromTheme("edit-delete"))
        delete_btn.setFixedSize(24, 24)
        delete_btn.setStyleSheet("border: none;")
        delete_btn.clicked.connect(lambda: self.delete_clicked.emit(task["id"]))
        btn_layout.addWidget(delete_btn)

        layout.addLayout(btn_layout)

        self.setStyleSheet("""
            QWidget {
                background-color: #f9f9f9;
                border: 1px solid #ccc;
                border-radius: 8px;
            }
            QWidget:hover {
                background-color: #f0f0f0;
            }
        """)
