import sys

from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.cre_btn.clicked.connect(self.run)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        print(2)
        # Имя элемента совпадает с objectName в QTDesigner


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())