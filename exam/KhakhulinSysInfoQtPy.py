import platform
import time
import psutil
from PySide6 import QtWidgets, QtCore
from psutil._common import bytes2human

from exam.ui.SysInfoForm import Ui_Form


class SysInfoWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.SystemInfo = SystemInfo()
        self.WinProcesses = WinProcesses()
        self.WinServices = WinServices()
        self.__initThreads()
        self.__initUi()
        self.__initSignals()

    def __initThreads(self):
        self.SystemInfo.start()
        self.WinProcesses.start()
        self.WinServices.start()

    def __initUi(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def __initSignals(self):
        self.ui.delayTimeLineEdit.textChanged.connect(self.delayTimeLineEditTextChanged)
        self.SystemInfo.systemInfoReceived.connect(self.onSystemInfoReceived)
        self.WinProcesses.WinProcessesReceived.connect(self.onWinProcessesReceived)
        self.WinServices.WinServicesReceived.connect(self.onWinServicesReceived)

    def delayTimeLineEditTextChanged(self, text):
        if text:
            self.SystemInfo.delay = int(self.ui.delayTimeLineEdit.text())
        else:
            self.SystemInfo.delay = 1

    def onSystemInfoReceived(self, params):
        self.ui.CpuInfoLabel.setText(str(f"Модель процессора: {params[0]}"))
        self.ui.CpuCoresLabel.setText(str(f"Количество логических и физических процессоров: {params[1]}"))
        self.ui.CpuUsageLabel.setText(str(f"Загрузка процессора: {params[2]}%"))
        self.ui.TotalRamLabel.setText(str(f"Объём памяти: {bytes2human(params[3])}"))
        self.ui.RamUsageLabel.setText(str(f"Загрузка виртуальной памяти: {params[4]}%"))
        self.ui.HddInfoBoxplainTextEdit.setPlainText(f"Количество дисков:{params[5]} \n")
        self.ui.HddInfoBoxplainTextEdit.appendPlainText(f"Информация о дисках: \n {params[6]}")

    def onWinProcessesReceived(self, params):
        self.ui.WinProcessesPlainTextEdit.setPlainText(str("params"))

    def onWinServicesReceived(self, params):
        self.ui.WinServicesPlainTextEdit.setPlainText(str("params"))


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def setDelay(self, delay) -> None:
        if delay:
            self.delay = int(delay)
        else:
            self.delay = 5

    def run(self):
        if self.delay is None:
            self.delay = 5

        while True:
            cpu_name = platform.processor()  # модель процессора
            cpu_cores = psutil.cpu_count()  # количество логических и физических процессоров(ядер)
            cpu_load = psutil.cpu_percent()  # загрузка CPU
            ram_total = psutil.virtual_memory().total
            ram_load = psutil.virtual_memory().percent  # загрузка RAM
            disc_counter = len(psutil.disk_partitions(all=False))
            hdd_info = []
            for hdd in psutil.disk_partitions(all=False):
                usage = psutil.disk_usage(hdd.mountpoint)
                hdd_info.append(("Диск:", hdd.device, "Объём диска:", bytes2human(usage.total), "Занято на диске:", bytes2human(usage.used)))

            self.systemInfoReceived.emit([cpu_name, cpu_cores, cpu_load, ram_total, ram_load, disc_counter, hdd_info])
            time.sleep(self.delay)


class WinProcesses(QtCore.QThread):
    WinProcessesReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = 20

    def run(self) -> None:
        while True:
            win_processes = list(psutil.process_iter())
            self.WinProcessesReceived.emit(win_processes)
            time.sleep(self.delay)


class WinServices(QtCore.QThread):
    WinServicesReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = 20

    def run(self) -> None:
        while True:
            win_services = list(psutil.win_service_iter())
            self.WinServicesReceived.emit(win_services)
            time.sleep(self.delay)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = SysInfoWindow()
    window.show()

    app.exec()
