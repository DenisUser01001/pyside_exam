"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""
import time

from PySide6 import QtWidgets

from lab_3.b_laboratory.a_threads import WeatherHandler


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initThreads()
        self.__initUi()
        self.__initSignals()

    def __initThreads(self):
        self.thread = WeatherHandler()

    def __initUi(self):
        self.setMinimumSize(600, 400)
        self.latLineEdit = QtWidgets.QLineEdit()
        self.latLineEdit.setPlaceholderText("Укажите широту:")
        self.lonLineEdit = QtWidgets.QLineEdit()
        self.lonLineEdit.setPlaceholderText("Укажите долготу:")
        self.delayTimeLineEdit = QtWidgets.QLineEdit()
        self.delayTimeLineEdit.setPlaceholderText("Укажите время задержки:")
        self.infoBoxPlainTextEdit = QtWidgets.QPlainTextEdit()
        self.infoBoxPlainTextEdit.setReadOnly(True)
        self.threadStartStopButton = QtWidgets.QPushButton("Старт/Стоп")
        self.threadStartStopButton.setCheckable(True)

        l_handle = QtWidgets.QVBoxLayout()
        l_handle.addWidget(self.latLineEdit)
        l_handle.addWidget(self.lonLineEdit)
        l_handle.addWidget(self.delayTimeLineEdit)
        l_handle.addWidget(self.threadStartStopButton)

        layout = QtWidgets.QHBoxLayout()
        layout.addLayout(l_handle)
        layout.addWidget(self.infoBoxPlainTextEdit)

        self.setLayout(layout)

    def __initSignals(self):
        self.threadStartStopButton.clicked.connect(self.onThreadStartStopButton)
        self.thread.weatherInfoReceived.connect(self.sendWeatherReportOnDisplay)

    def onThreadStartStopButton(self, status):
        self.threadStartStopButton.setText("Стоп" if status else "Старт")

        if not status:
            self.thread.stop()
            self.latLineEdit.setEnabled(True)
            self.lonLineEdit.setEnabled(True)
            self.delayTimeLineEdit.setEnabled(True)
        else:
            self.thread.setStatus(True)
            self.thread.setDelay(self.delayTimeLineEdit.text())
            self.thread.setCoordinates(int(self.latLineEdit.text()), int(self.lonLineEdit.text()))
            self.thread.start()
            self.latLineEdit.setEnabled(False)
            self.lonLineEdit.setEnabled(False)
            self.delayTimeLineEdit.setEnabled(False)

    def sendWeatherReportOnDisplay(self, data):
        # print(data)

        self.infoBoxPlainTextEdit.setPlainText(f"Текущее время:\n {time.ctime()}\n\nПолученная информация:\n {data}")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

