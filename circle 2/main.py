import sys
import random
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.circle = Circle()
        self.setCentralWidget(self.circle)


class Circle(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('круги 2.0')
        self.circles = []
        self.pushbutton = QPushButton('Кнопка', self)
        self.pushbutton.clicked.connect(self.add_circle)
        self.pushbutton.resize(150, 30)

    def add_circle(self):
        d = random.randint(20, 100)
        x = random.randint(0, self.width() - d)
        y = random.randint(0, self.height() - d)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, d, color))
        self.repaint()

    def paintEvent(self, event):
        paint = QPainter(self)
        for x, y, d, color in self.circles:
            paint.setBrush(color)
            paint.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())