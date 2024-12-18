import platform
import time
import psutil
#  pip install pywin32
import win32com.client
from PySide6 import QtWidgets, QtCore
from psutil._common import bytes2human

from exam.ui.SysInfoForm import Ui_Form


class SysInfoWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.SystemInfo = SystemInfo()
        self.WinProcesses = WinProcesses()
        self.WinServices = WinServices()
        self.WinScheduler = WinScheduler()
        self.__initThreads()
        self.__initUi()
        self.__initSignals()

    def __initThreads(self):
        self.SystemInfo.start()
        self.WinProcesses.start()
        self.WinServices.start()
        self.WinScheduler.start()

    def __initUi(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def __initSignals(self):
        self.ui.delayTimeLineEdit.textChanged.connect(self.delayTimeLineEditTextChanged)
        self.SystemInfo.systemInfoReceived.connect(self.onSystemInfoReceived)
        self.WinProcesses.WinProcessesReceived.connect(self.onWinProcessesReceived)
        self.WinServices.WinServicesReceived.connect(self.onWinServicesReceived)
        self.WinScheduler.WinSchedulerReceived.connect(self.onWinSchedulerReceived)

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
        self.ui.HddInfoBoxplainTextEdit.setPlainText(f"Количество дисков: {params[5]} \n")
        self.ui.HddInfoBoxplainTextEdit.appendPlainText(f"Информация о дисках: \n")
        for x in params[6]:
            self.ui.HddInfoBoxplainTextEdit.appendPlainText(str(x))

    def onWinProcessesReceived(self, params):
        # self.ui.WinProcessesPlainTextEdit.setPlainText(str(params))
        for x in params:
            self.ui.WinProcessesPlainTextEdit.appendPlainText(str(x))

    def onWinServicesReceived(self, params):
        # self.ui.WinServicesPlainTextEdit.setPlainText(str(params))
        for x in params:
            self.ui.WinServicesPlainTextEdit.appendPlainText(str(x))

    def onWinSchedulerReceived(self, params):
        # self.ui.WinShedulePlainTextEdit.setPlainText(str(params))
        for x in params:
            self.ui.WinShedulePlainTextEdit.appendPlainText(str(x))

    def closeEvent(self, event):
        ...


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
                try:
                    usage = psutil.disk_usage(hdd.mountpoint)
                    hdd_info.append(("Диск:", hdd.device, "Объём диска:", bytes2human(usage.total), "Занято на диске:", bytes2human(usage.used)))
                except PermissionError:
                    continue
            self.systemInfoReceived.emit([cpu_name, cpu_cores, cpu_load, ram_total, ram_load, disc_counter, hdd_info])
            time.sleep(self.delay)


class WinProcesses(QtCore.QThread):
    WinProcessesReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = 20

    def run(self) -> None:
        while True:
            win_processes = []
            for proc in psutil.process_iter():
                # proc_info = dict()
                with proc.oneshot():
                    # proc_info["pid"] = proc.pid
                    # proc_info["ppid"] = proc.ppid()
                    # proc_info["name"] = proc.name()
                    # proc_info["exe"] = proc.exe()  # Requires root access for '/proc/#/exe'
                    # proc_info["cpu_percent"] = proc.cpu_percent()
                    # mem_info = proc.memory_info()
                    # proc_info["mem_rss"] = mem_info.rss
                    # proc_info["num_threads"] = proc.num_threads()
                    # proc_info["nice_priority"] = proc.nice()
                    # win_processes.append([proc.pid, proc.name()])
                    win_processes.append(proc.name())
            self.WinProcessesReceived.emit(win_processes)
            time.sleep(self.delay)
        # while True:
            # win_processes = list(psutil.process_iter())
            # self.WinProcessesReceived.emit(win_processes)
            # time.sleep(self.delay)


class WinServices(QtCore.QThread):
    WinServicesReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = 20

    def run(self) -> None:
        while True:
            win_services = []
            for serv in psutil.win_service_iter():
                win_services.append(serv.name())
            self.WinServicesReceived.emit(win_services)
            time.sleep(self.delay)

        # while True:
        #     win_services = list(psutil.win_service_iter())
        #     self.WinServicesReceived.emit(win_services)
        #     time.sleep(self.delay)


class WinScheduler(QtCore.QThread):
    WinSchedulerReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = 20

    def run(self) -> None:
        TASK_STATE = {0: 'Unknown',
                      1: 'Disabled',
                      2: 'Queued',
                      3: 'Ready',
                      4: 'Running'}
        while True:
            win_scheduler = []
            scheduler = win32com.client.Dispatch('Schedule.Service')
            scheduler.Connect()
            folders = [scheduler.GetFolder('\\')]
            while folders:
                folder = folders.pop(0)
                folders += list(folder.GetFolders(0))
                for task in folder.GetTasks(0):
                    win_scheduler.append(["Название: ", task.name, "Путь: ", task.path, "Состояние: ", TASK_STATE[task.state]])
            self.WinSchedulerReceived.emit(win_scheduler)
            time.sleep(self.delay)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = SysInfoWindow()
    window.show()

    app.exec()
