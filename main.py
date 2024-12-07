import sys
from random import randint
from PyQt6.QtCore import QRectF, QPointF, QSizeF, Qt
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QMainWindow


class YCircle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.qp = QPainter()
        self.color = QColor(255, 0, 0)
        self.initUI()

    def paintEvent(self, event):
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        # qp.setBrush(QColor(0, 255, 255))
        qp.setPen(QPen(Qt.GlobalColor.yellow))
        diameter = randint(0, 300)
        x, y = self.geometry().size().width() / 2, self.geometry().size().height() / 2
        qp.drawEllipse(QPointF(x, y), diameter, diameter)
        qp.end()

    def initUI(self):
        self.setWindowTitle('Get Yellow Circles')
        self.btn = self.pushButton
        self.btn.clicked.connect(self.update)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YCircle()
    ex.show()
    sys.exit(app.exec())
