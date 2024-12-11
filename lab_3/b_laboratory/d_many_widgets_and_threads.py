"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""

from PySide6 import QtWidgets

from lab_3.b_laboratory.b_systeminfo_widget import SysInfoWidget
from lab_3.b_laboratory.c_weatherapi_widget import WeatherInfoWidget


class SummaryWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()

    def __initUi(self):
        self.setMinimumSize(1000, 450)
        self.sysInfoWidget = SysInfoWidget()
        self.weatherInfoWidget = WeatherInfoWidget()

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.sysInfoWidget)
        layout.addWidget(self.weatherInfoWidget)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = SummaryWindow()
    window.show()

    app.exec()


