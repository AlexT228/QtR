import sys
from random import randint

from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.cre_btn.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ell(qp)
            qp.end()
        self.do_paint = False


    def run(self):
        self.do_paint = True
        self.update()


    def draw_ell(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x = randint(1, 100)
        qp.drawEllipse(int(150 - x/2), int(150 - x/2), x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())