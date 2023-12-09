import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QAction
from PyQt5.QtGui import QPainter, QPen, QImage, QIcon
from PyQt5.QtCore import Qt, QPoint


class DrawingBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Handwriting Board')
        self.setFixedSize(280, 280)
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.last_pos = QPoint()
        self.drawing = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(self.rect(), self.image, self.image.rect())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_pos = event.pos()
            self.drawing = True

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(Qt.black, 10, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.last_pos, event.pos())
            self.last_pos = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.drawing:
            self.drawing = False

    def clearImage(self):
        self.image.fill(Qt.white)
        self.update()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Handwriting Board')
        self.board = DrawingBoard()
        self.setCentralWidget(self.board)
        self.create_menu()

    def create_menu(self):
        clear_action = self.create_action('Clear', self.board.clearImage, 'Ctrl+C')
        exit_action = self.create_action('Exit', self.close, 'Ctrl+Q')

        file_menu = self.menuBar().addMenu('File')
        self.add_actions(file_menu, [clear_action, exit_action])

    @staticmethod
    def create_action(text, slot=None, shortcut=None, icon=None, tip=None):
        action = QAction(text)
        if icon is not None:
            action.setIcon(QIcon(icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            action.triggered.connect(slot)
        return action

    @staticmethod
    def add_actions(target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())