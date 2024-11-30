import sys
import random
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('круги')
        self.circles = []
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        d = random.randint(20, 100)
        x = random.randint(0, self.width() - d)
        y = random.randint(0, self.height() - d)
        self.circles.append((x, y, d))
        self.update()

    def paintEvent(self, event):
        paint = QPainter(self)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        paint.setBrush(QColor(color))
        for x, y, d in self.circles:
            paint.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
