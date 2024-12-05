"""
Файл для повторения темы фильтр событий

Напомнить про работу с фильтром событий.

Предлагается создать кликабельный QLabel с текстом "Красивая кнопка",
используя html - теги, покрасить разные части текста на нём в разные цвета
(красивая - красным, кнопка - синим)
"""
import time

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__initUi()

    def __initUi(self):
        self.__label = QtWidgets.QLabel()
        self.__label.setText("<h3 style='color:green'> Военная </h3><h3 style='color:black'> кнопка </h3>")
        self.__label.setStyleSheet("border: 1px solid black; border-radius:3px")
        self.__label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # self.__label.clicked.connect(lambda: print("Фиг"))

        self.__label.installEventFilter(self)

        l = QtWidgets.QHBoxLayout()
        l.addWidget(self.__label)

        self.setLayout(l)

    def eventFilter(self, watched, event):
        # print(watched, event)
        if watched == self.__label:
            if event.type() == QtCore.QEvent.Type.Resize:
                # print("изменён размер окна")
                width = event.size().width()
                self.__label.setStyleSheet(f"border: 1px solid black; border-radius:3px; font-size: {int(width/20)}px")
            if event.type() == QtCore.QEvent.Type.MouseButtonPress:
                self.backendonclick()

        return super().eventFilter(watched, event)

    def backendonclick(self):
        print(time.ctime(), "--->", "button pressed")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
