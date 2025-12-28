import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("R3call")

        container = QWidget()
        self.setCentralWidget(container)

        main_layout = QVBoxLayout(container)

        vocabulary = QLabel("探索")
        vocabulary.setAlignment(Qt.AlignCenter)

        button_container = QWidget()
        button_layout = QHBoxLayout(button_container)

        pass_button = QPushButton("Pass")
        recall_button = QPushButton("Recall")

        button_layout.addWidget(pass_button)
        button_layout.addWidget(recall_button)

        main_layout.addWidget(vocabulary)
        main_layout.addWidget(button_container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())