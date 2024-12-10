"""
Файл для повторения темы QThread

Напомнить про работу с QThread.

Предлагается создать небольшое приложение, которое будет с помощью модуля request
получать доступность того или иного сайта (возвращать из потока status_code сайта).

Поработать с сигналами, которые возникают при запуске/остановке потока,
передать данные в поток (в данном случае url),
получить данные из потока (статус код сайта),
попробовать управлять потоком (запуск, остановка).

Опционально поработать с валидацией url
"""
import time
import traceback

import requests
from PySide6 import QtWidgets, QtCore

from lab_3.a_repeat.a_qtimer_repeat import ClockWidget


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()
        self.__initSignals()

    def __initUi(self):
        self.setStyleSheet("font-size: 20px")

        self.lineEditUrl = QtWidgets.QLineEdit()
        self.lineEditUrl.setPlaceholderText("Введите URL")

        self.pushButtonHandler = QtWidgets.QPushButton("Старт")
        self.pushButtonHandler.setCheckable(True)

        self.plainTextEditLog = QtWidgets.QPlainTextEdit()
        self.plainTextEditLog.setReadOnly(True)

        self.clock = ClockWidget()

        l_handle = QtWidgets.QHBoxLayout()
        l_handle.addWidget(self.lineEditUrl)
        l_handle.addWidget(self.pushButtonHandler)

        l = QtWidgets.QVBoxLayout()
        l.addLayout(l_handle)
        l.addWidget(self.plainTextEditLog)
        l.addWidget(self.clock)

        self.setLayout(l)

    def __initSignals(self):
        self.pushButtonHandler.clicked.connect(self.__handleMainThread)

    def __handleMainThread(self, status):
        # Желательно делать проверку на валидность url...
        self.pushButtonHandler.setText("Стоп" if status else "Старт")

        if not status:
            self.thread.stop()
        else:

            self.thread = MainThread(self.lineEditUrl.text())

            # self.thread.started.connect(lambda data: self.plainTextEditLog.appendPlainText(f"{time.ctime()} >>> Поток запущен"))
            self.thread.started.connect(lambda: self.appendLogMessage(">>> Поток запущен"))

            # self.thread.checked.connect(lambda data: self.plainTextEditLog.appendPlainText(f"{time.ctime()} >>> Статус код: {data}"))
            self.thread.checked.connect(lambda data: self.appendLogMessage(f"Статус код: {data}"))

            # self.thread.finished.connect(lambda data: self.plainTextEditLog.appendPlainText(f"{time.ctime()} >>> Поток остановлен"))
            self.thread.finished.connect(lambda: self.appendLogMessage(">>> Поток остановлен"))
            self.thread.finished.connect(lambda: self.pushButtonHandler.setChecked(False))
            self.thread.finished.connect(lambda: self.pushButtonHandler.setText("Старт"))
            self.thread.start()

    def appendLogMessage(self, text):
        self.plainTextEditLog.appendPlainText(f"{time.ctime()} >>> {text}")


class MainThread(QtCore.QThread):
    checked = QtCore.Signal(int)

    def __init__(self, url, delay=1, parent=None):
        super().__init__(parent)
        self.url = url
        self.__status = None
        self.__delay = delay

    def stop(self):
        self.__status = False

    def setDelay(self, delay):
        self.__delay = delay

    def run(self):
        self.__status = True
        while self.__status:
            try:
                r = requests.get(self.url, timeout=3)
                self.checked.emit(r.status_code)
                self.sleep(self.__delay)
            except Exception:
                traceback.print_exc()
                self.stop()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
