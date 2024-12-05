"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__initUi()
        self.__initSignals()

    def __initUi(self):
        self.lineEditInput = QtWidgets.QLineEdit()
        self.lineEditMirror = QtWidgets.QLineEdit()
        self.lineEditMirror.setReadOnly(True)

        self.pushButtonMirror = QtWidgets.QPushButton('Mirror')
        self.pushButtonClear = QtWidgets.QPushButton('Clear')

        l_lineedit = QtWidgets.QHBoxLayout()
        l_lineedit.addWidget(self.lineEditInput)
        l_lineedit.addWidget(self.lineEditMirror)

        l_pushbutton = QtWidgets.QHBoxLayout()
        l_pushbutton.addWidget(self.pushButtonMirror)
        l_pushbutton.addWidget(self.pushButtonClear)

        l_main = QtWidgets.QVBoxLayout()
        l_main.addLayout(l_lineedit)
        l_main.addLayout(l_pushbutton)

        self.setLayout(l_main)

    def __initSignals(self):
        self.pushButtonMirror.clicked.connect(self.__onPushButtonMirrorClicked)
        self.pushButtonClear.clicked.connect(self.__onPushButtonClearClicked)
        # self.lineEditInput.textChanged.connect(self.__onPushButtonMirrorClicked)
        self.lineEditInput.textChanged.connect(self.__onLineEditMirrorTextChanged)

    def __onPushButtonMirrorClicked(self):
        self.lineEditMirror.setText(self.lineEditInput.text()[::-1])
        # print(self.lineEditInput.text())

    def __onPushButtonClearClicked(self):
        # print("Нажата кнопка Clear")
        self.lineEditMirror.clear()
        self.lineEditInput.clear()
    def __onLineEditMirrorTextChanged(self, text):
        self.lineEditMirror.setText(text[::-1])


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
