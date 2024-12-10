"""
Файл для повторения темы QTimer

Напомнить про работу с QTimer.

Предлагается создать приложение-которое будет
с некоторой периодичностью вызывать определённую функцию.
"""
import time

from PySide6 import QtWidgets, QtCore


class ClockWidget(QtWidgets.QDateTimeEdit):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.showCurrentDateTime()
        self.__initUi()
        self.__initTimer()

    # def event(self, event):
    #     if event.type() == QtCore.QEvent.Type.Resize:
    #         print(event.size())
    #     return super().event(event)


    def __initUi(self):
        self.setMinimumSize(300, 80)
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("color: blue; font-size: 30px; font-weight: 600")
        self.setDisplayFormat("dd.MM.yyyy HH:mm:ss")
        self.setEnabled(False)


    def __initTimer(self):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.showCurrentDateTime)
        # self.timer.setSingleShot(True)
        self.timer.start()

    def showCurrentDateTime(self):
        current_datetime = QtCore.QDateTime.currentDateTime()
        self.setDateTime(current_datetime)
        # print(current_datetime.toPython())




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    widget = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout()
    label = QtWidgets.QLabel("Текущая дата и время")
    clock = ClockWidget()

    layout.addWidget(clock)
    layout.addWidget(label)

    widget.setLayout(layout)
    widget.show()

    # window.show()

    app.exec()
