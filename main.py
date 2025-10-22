from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow
import sys
from controllers.task_controller import TaskController

app = QApplication(sys.argv)
window = MainWindow()
controller = TaskController(window)
window.show()
sys.exit(app.exec())
