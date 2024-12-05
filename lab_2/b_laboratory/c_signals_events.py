"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущий основной монитор
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""
import time

from PySide6 import QtWidgets, QtCore, QtGui

from lab_2.b_laboratory.ui.c_signals_events_form import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.__initSignals()

        # screen params:
        screens = QtGui.QGuiApplication.screens()
        # print(f'Количество экранов (мониторов): {len(screens)}')
        # print(f'Текущий основной монитор (модель): {QtGui.QGuiApplication.primaryScreen().name()}')
        # print(f'Разрешение основного экрана: {screens[1].size().width()} * {screens[1].size().height()}')
        # print(f'Окно приложения отображается на мониторе: {QtGui.QGuiApplication.screenAt(self.pos()).name()}')
        # print(f'Размеры окна в пикселях: {self.size().width()} * {self.size().height()}')
        # print(f'Минимальные размеры окна: {self.minimumSize().width()} * {self.minimumSize().height()}')
        # print(f'Текущее положение (координаты) окна: {self.pos().x()},{self.pos().y()}')
        # print(f'Координаты центра приложения (центра окна приложения): {self.pos().x() + self.size().width()/2},{self.pos().y() + self.size().height()/2}')
        # print(f'Состояние окна приложения:\n'
        #       f'Окно свёрнуто: {QtWidgets.QWidget.isMinimized(self.window())}\n'
        #       f'Окно развёрнуто: {QtWidgets.QWidget.isMaximized(self.window())}\n'
        #       f'Окно активно: {QtWidgets.QWidget.isActiveWindow(self.window())}\n'
        #       f'Окно отображено: {QtWidgets.QWidget.isVisible(self.window())}')

        self.screen_width = screens[1].availableSize().width()
        self.screen_height = screens[1].availableSize().height()

        # Разрешение экрана другим способом:
        # self.screen_width = QtWidgets.QApplication.primaryScreen().size().width()
        # self.screen_height = QtWidgets.QApplication.primaryScreen().size().height()

        # window params
        # self.window_width = QtWidgets.QWidget.geometry()
        self.window_width = self.geometry().width()
        self.window_height = self.geometry().height()

    def __initSignals(self):
        self.ui.pushButtonLT.clicked.connect(self.onpushButtonLTclicked)
        self.ui.pushButtonRT.clicked.connect(self.onpushButtonRTclicked)
        self.ui.pushButtonCenter.clicked.connect(self.onpushButtonCenterclicked)
        self.ui.pushButtonLB.clicked.connect(self.onpushButtonLBclicked)
        self.ui.pushButtonRB.clicked.connect(self.onpushButtonRBclicked)
        self.ui.pushButtonMoveCoords.clicked.connect(self.onpushButtonMoveCoordsclicked)
        self.ui.pushButtonGetData.clicked.connect(self.onpushButtonGetDataclicked)

    @QtCore.Slot()
    def onpushButtonLTclicked(self):
        self.move(0, 0)

    @QtCore.Slot()
    def onpushButtonRTclicked(self):
        self.move((self.screen_width - self.window_width), 0)

    @QtCore.Slot()
    def onpushButtonCenterclicked(self):
        self.move(int((self.screen_width - self.window_width)/2), int((self.screen_height - self.window_height)/2))

    @QtCore.Slot()
    def onpushButtonLBclicked(self):
        self.move(0, (self.screen_height-self.window_height))

    @QtCore.Slot()
    def onpushButtonRBclicked(self):
        self.move((self.screen_width - self.window_width), (self.screen_height-self.window_height))

    @QtCore.Slot()
    def onpushButtonMoveCoordsclicked(self):
        self.move(int(self.ui.spinBoxX.text()), int(self.ui.spinBoxY.text()))

    @QtCore.Slot()
    def onpushButtonGetDataclicked(self):
        screens = QtGui.QGuiApplication.screens()
        app_params = (f'Текущее время: {time.ctime()}\n'
            f'Количество экранов (мониторов): {len(screens)}\n'
            f'Текущий основной монитор (модель): {QtGui.QGuiApplication.primaryScreen().name()}\n'
            f'Разрешение основного экрана: {screens[1].size().width()} * {screens[1].size().height()}\n'
            f'Окно приложения отображается на мониторе: {QtGui.QGuiApplication.screenAt(self.pos()).name()}\n'
            f'Размеры окна в пикселях: {self.size().width()} * {self.size().height()}\n'
            f'Минимальные размеры окна: {self.minimumSize().width()} * {self.minimumSize().height()}\n'
            f'Текущее положение (координаты) окна: {self.pos().x()},{self.pos().y()}\n'
            f'Координаты центра приложения (центра окна приложения): {self.pos().x() + self.size().width() / 2},{self.pos().y() + self.size().height() / 2}\n'
            f'Состояние окна приложения:\n'
            f'Окно свёрнуто: {QtWidgets.QWidget.isMinimized(self.window())}\n'
            f'Окно развёрнуто: {QtWidgets.QWidget.isMaximized(self.window())}\n'
            f'Окно активно: {QtWidgets.QWidget.isActiveWindow(self.window())}\n'
            f'Окно отображено: {QtWidgets.QWidget.isVisible(self.window())}')
        self.ui.plainTextEdit.setPlainText(app_params)

    def moveEvent(self, event):
        print(f'{time.ctime()}: Текущая позиция: {event.pos().x(), event.pos().y()}, Предыдущая позиция: {event.oldPos().x(), event.oldPos().y()} ')


    def resizeEvent(self, event):
        print(f'{time.ctime()}: Текущий размер окна приложения: {event.size().width(), event.size().height()} ')


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
