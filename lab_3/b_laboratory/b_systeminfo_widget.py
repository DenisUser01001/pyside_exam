"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
import psutil
from PySide6 import QtWidgets

from lab_3.b_laboratory.a_threads import SystemInfo


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initThread()
        self.__initUi()
        self.__initSignals()
        self.thread.start()

    def __initThread(self):
        self.thread = SystemInfo()

    def __initUi(self):
        self.setMinimumSize(300, 100)
        self.delayTimeLineEdit = QtWidgets.QLineEdit()
        self.delayTimeLineEdit.setPlaceholderText("Укажите время задержки (по умолчанию - 1 сек)")

        self.CpuUsageLabel = QtWidgets.QLabel()
        self.RamUsageLabel = QtWidgets.QLabel()

        l = QtWidgets.QVBoxLayout()
        l.addWidget(self.delayTimeLineEdit)
        l.addWidget(self.CpuUsageLabel)
        l.addWidget(self.RamUsageLabel)

        self.setLayout(l)

    def __initSignals(self):
        self.delayTimeLineEdit.textChanged.connect(self.delayTimeLineEditTextChanged)
        self.thread.systemInfoReceived.connect(self.onsystemInfoReceived)

    def delayTimeLineEditTextChanged(self, text):
        if text:
            self.thread.delay = int(self.delayTimeLineEdit.text())
        else:
            self.thread.delay = 1

    def onsystemInfoReceived(self, params):
        self.CpuUsageLabel.setText(str(f"Загрузка процессора: {params[0]}%"))
        self.RamUsageLabel.setText(str(f"Загрузка виртуальной памяти: {params[1]}%"))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

