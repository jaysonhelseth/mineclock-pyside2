import sys
from datetime import datetime

from PySide2 import QtCore
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QApplication, QMainWindow

from gui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.update_time()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_time)
        self.timer.start()

        self.closeButton.clicked.connect(app.exit)
        self.closeButton.setVisible(False)
        self.setWindowState(QtCore.Qt.WindowState.WindowFullScreen)

        self.change_size(self.mainClock, 335)
        self.change_size(self.day, 55)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_BracketLeft:
            self.change_size_incremental(self.mainClock, 1)
        elif event.key() == QtCore.Qt.Key_BracketRight:
            self.change_size_incremental(self.mainClock, -1)
        elif event.key() == QtCore.Qt.Key_Semicolon:
            self.change_size_incremental(self.day, 1)
        elif event.key() == QtCore.Qt.Key_Apostrophe:
            self.change_size_incremental(self.day, -1)
        self.print_size()

    def change_size_incremental(self, label, number):
        font = label.font()
        new_size = font.pointSize() + number
        font.setPointSize(new_size)
        label.setFont(font)

    def change_size(self, label, number):
        font = label.font()
        font.setPointSize(number)
        label.setFont(font)

    def print_size(self):
        print(f"MainClock: {self.mainClock.font().pointSize()}, Day: {self.day.font().pointSize()}")

    def update_time(self):
        now = datetime.now()
        self.mainClock.setText(now.strftime("%I:%M"))
        self.day.setText(now.strftime("%p %a"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
