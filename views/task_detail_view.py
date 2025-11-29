# views/task_detail_view.py
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QComboBox, QHBoxLayout,
    QFileDialog, QMessageBox, QSpacerItem, QSizePolicy
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal
import os
import shutil
from PIL import Image

class TaskDetailView(QWidget):
    """Vue détaillée d'une tâche (édition, description, image, statut)."""

    upload_clicked = Signal(object)
    back_clicked = Signal()
    status_changed = Signal(str)
    save_clicked = Signal(dict)

    def __init__(self, task: dict, parent=None, parent_controller=None):
        super().__init__(parent)
        self.task = task
        self.parent_controller = parent_controller
        self.setup_ui()

    def setup_ui(self):
        """Configure l'interface utilisateur."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # === Titre + Retour ===
        header = QHBoxLayout()
        back_btn = QPushButton("← Retour")
        back_btn.setFixedWidth(100)
        back_btn.clicked.connect(self.back_clicked.emit)

        title_label = QLabel(self.task["title"])
        title_label.setStyleSheet("font-size: 20px; font-weight: bold;")

        header.addWidget(back_btn)
        header.addStretch()
        header.addWidget(title_label)
        layout.addLayout(header)

        # === Image bannière ===
        self.setup_banner_section(layout)

        # === Description ===
        self.setup_description_section(layout)

        # === Statut ===
        self.setup_status_section(layout)

        # === Bouton de sauvegarde ===
        self.setup_save_button(layout)

        # Style global
        self.setStyleSheet(self.get_stylesheet())

    def setup_banner_section(self, layout):
        """Configure la section de la bannière."""
        self.banner = QLabel()
        self.banner.setAlignment(Qt.AlignCenter)
        self.banner.setFixedHeight(160)
        self.banner.setStyleSheet("background-color: #f1f1f1; border-radius: 10px;")

        if self.task.get("image_path") and os.path.exists(self.task["image_path"]):
            pix = QPixmap(self.task["image_path"])
            self.banner.setPixmap(pix.scaledToHeight(160, Qt.SmoothTransformation))
        else:
            self.banner.setText("🖼️ Aucune image")

        layout.addWidget(self.banner)

        # Boutons pour la bannière
        banner_btn_layout = QHBoxLayout()
        upload_btn = QPushButton("Changer la bannière")
        upload_btn.clicked.connect(self.upload_banner)

        clear_btn = QPushButton("Supprimer")
        clear_btn.clicked.connect(self.clear_banner)
        clear_btn.setVisible(bool(self.task.get("image_path")))

        banner_btn_layout.addStretch()
        banner_btn_layout.addWidget(upload_btn)
        banner_btn_layout.addWidget(clear_btn)
        layout.addLayout(banner_btn_layout)

        # Stocker le bouton clear pour le mettre à jour plus tard
        self.clear_banner_btn = clear_btn

    def setup_description_section(self, layout):
        """Configure la section de description."""
        desc_label = QLabel("📝 Description :")
        layout.addWidget(desc_label)

        self.description_edit = QTextEdit()
        self.description_edit.setPlaceholderText("Décris la tâche en détail...")
        self.description_edit.setText(self.task.get("description", ""))
        layout.addWidget(self.description_edit)

    def setup_status_section(self, layout):
        """Configure la section de statut."""
        status_layout = QHBoxLayout()
        status_label = QLabel("Statut :")
        status_layout.addWidget(status_label)

        self.status_colors = {
            "À faire": "#ffb347",
            "En cours": "#6fa3ef",
            "Terminée": "#77dd77"
        }

        self.status_box = QComboBox()
        for status, color in self.status_colors.items():
            self.status_box.addItem(status)
            index = self.status_box.findText(status)
            self.status_box.setItemData(index, color, Qt.BackgroundRole)

        self.status_box.setCurrentText(self.task["status"])
        self.status_box.currentTextChanged.connect(self.status_changed.emit)
        status_layout.addWidget(self.status_box)
        layout.addLayout(status_layout)

    def setup_save_button(self, layout):
        """Configure le bouton de sauvegarde."""
        save_btn = QPushButton("💾 Enregistrer")
        save_btn.clicked.connect(self.save_task)
        layout.addWidget(save_btn, alignment=Qt.AlignRight)

    def get_stylesheet(self):
        """Retourne la feuille de style pour le widget."""
        return """
            QPushButton {
                background-color: #f5f5f5;
                border: 1px solid #ccc;
                border-radius: 6px;
                padding: 6px 10px;
            }
            QPushButton:hover {
                background-color: #e9e9e9;
            }
            QTextEdit {
                background: #fff;
                border: 1px solid #ccc;
                border-radius: 6px;
                padding: 8px;
                font-size: 13px;
            }
            QComboBox {
                background: #fff;
                border: 1px solid #ccc;
                border-radius: 6px;
                padding: 5px;
            }
        """

    def upload_banner(self):
        """Gère l'upload d'une nouvelle bannière."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Sélectionner une bannière",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )

        if not file_path:
            return

        try:
            # Créer le dossier images/ s'il n'existe pas
            image_dir = "images"
            os.makedirs(image_dir, exist_ok=True)

            # Générer un nom de fichier unique
            image_filename = f"task_{self.task['id']}_banner.png"
            dest_path = os.path.join(image_dir, image_filename)

            # Copier et redimensionner l'image
            shutil.copy2(file_path, dest_path)
            img = Image.open(dest_path)
            img.thumbnail((800, 300))
            img.save(dest_path)

            # Mettre à jour la tâche
            self.task["image_path"] = dest_path

            # Mettre à jour l'affichage
            pix = QPixmap(dest_path)
            self.banner.setPixmap(pix.scaledToHeight(160, Qt.SmoothTransformation))
            self.banner.setText("")

            # Activer le bouton de suppression
            self.clear_banner_btn.setVisible(True)

            # Notifier le contrôleur
            if self.parent_controller:
                self.parent_controller.update_task(self.task)
                self.upload_clicked.emit(self.task)

        except Exception as e:
            QMessageBox.warning(self, "Erreur", f"Impossible d'uploader l'image : {e}")

    def clear_banner(self):
        """Supprime la bannière actuelle."""
        try:
            if "image_path" in self.task and self.task["image_path"] and os.path.exists(self.task["image_path"]):
                os.remove(self.task["image_path"])

            # Mettre à jour la tâche et l'affichage
            self.task["image_path"] = None
            self.banner.setText("🖼️ Aucune image")
            self.clear_banner_btn.setVisible(False)

            # Notifier le contrôleur
            if self.parent_controller:
                self.parent_controller.update_task(self.task)

        except Exception as e:
            QMessageBox.warning(self, "Erreur", f"Impossible de supprimer l'image : {e}")

    def save_task(self):
        """Sauvegarde les modifications de la tâche."""
        updated_task = {
            "id": self.task["id"],
            "title": self.task["title"],  # Le titre n'est pas modifiable ici
            "description": self.description_edit.toPlainText(),
            "status": self.status_box.currentText(),
            "image_path": self.task.get("image_path")
        }
        self.save_clicked.emit(updated_task)
