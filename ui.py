import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QMessageBox, QDialog
from PySide6.QtCore import Qt
from utils import Access_db

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # dbからランダムなデータを３つもらい、listにする
        # list構成
        # [(id,word,pronunciation,meaning,count),...]
        self.data = Access_db()
        self.words = self.data.select_3words()
        self.word_index = 0

        # GUI
        '''
        MainWindow
        ├─ container (QWidget)
            ├─ main_layout (QVBoxLayout)
                ├─ word_label (QLabel)
                ├─ button_container (QWidget)
                    ├─ button_layout (QHBoxLayout)
                        ├─ pass_button (QPushButton)
                        ├─ recall_button (QPushButton)
        '''
        self.setWindowTitle("R3call")

        container = QWidget()
        self.setCentralWidget(container)

        main_layout = QVBoxLayout(container)

        self.word_label = QLabel(self.words[self.word_index][1])
        self.word_label.setAlignment(Qt.AlignCenter)

        button_container = QWidget()
        button_layout = QHBoxLayout(button_container)

        pass_button = QPushButton("Pass")
        pass_button.clicked.connect(self.pass_button_function)
        recall_button = QPushButton("Recall")
        recall_button.clicked.connect(self.recall_button_function)

        button_layout.addWidget(pass_button)
        button_layout.addWidget(recall_button)

        main_layout.addWidget(self.word_label)
        main_layout.addWidget(button_container)

    def closeEvent(self,event):
        # dbを閉じてから終了
        self.data.conn.close()
        print(event,"종료!!!")
        event.accept()

    def pass_button_function(self):
        self.next_or_quit()

    def recall_button_function(self):
        # self.show_word_info()
        self.next_or_quit()
    
    def next_or_quit(self):
        self.word_index += 1
        # 単語を３つ見せ終わったら
        if self.word_index == 3:
            QApplication.quit()
        else:
            self.word_label.setText(self.words[self.word_index][1])
    
    #Todo. 今は使わない
    def show_word_info(self):
        word, pronunciation, meaning = self.words[self.word_index][1:4]

        dialog = QDialog(self)

        dialog.setWindowTitle(f"info")

        layout = QVBoxLayout(dialog)
        info_label = QLabel(f"word : {word}\npronunciation : {pronunciation}\nmeaning : {meaning}")
        layout.addWidget(info_label)

        dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())