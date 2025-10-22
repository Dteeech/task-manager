from PySide6.QtWidgets import QApplication, QLabel

def main():
    app = QApplication([])
    label = QLabel("Bonjour PySide6 !")
    label.resize(200, 100)
    label.show()
    app.exec()

if __name__ == "__main__":
    main()
