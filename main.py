import sys
from random import randint
from PyQt6.QtCore import QRectF, QPointF, QSizeF, Qt
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QMainWindow


class UI(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Get Yellow Circles')
        self.setGeometry(300, 300, 900, 900)
        self.button = QPushButton("перерисовать", self)
        self.button.setGeometry(10, 10, 100, 20)


class YCircle(QMainWindow, UI):
    def __init__(self):
        self.setup()
        super().__init__()
        self.qp = QPainter()
        self.button.clicked.connect(self.button_clicked)

    def setup(self):
        self.color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.diameter = randint(0, 300)

    def button_clicked(self):
        self.update()
        self.setup()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(self.color)
        x, y = self.geometry().size().width() / 2, self.geometry().size().height() / 2
        qp.drawEllipse(QPointF(x, y), self.diameter, self.diameter)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YCircle()
    ex.show()
    sys.exit(app.exec())
