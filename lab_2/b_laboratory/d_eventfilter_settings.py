"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings_form.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore
from lab_2.b_laboratory.ui.d_eventfilter_settings_form import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.__initSignals()

    def __initSignals(self):
        self.ui.dial.valueChanged.connect(self.onChangeDialClicked)
        self.ui.comboBox.textActivated.connect(self.onCobmoBoxClicked)
        self.ui.horizontalSlider.valueChanged.connect(self.onHorizontalSliderClicked)

    def keyPressEvent(self, event):
        if event.text() == "+" and self.ui.dial.value() in range(0, 99):
            self.ui.dial.setValue(self.ui.dial.value() + 1)
        elif event.text() == '-' and self.ui.dial.value() in range(1, 100):
            self.ui.dial.setValue(self.ui.dial.value() - 1)

    @QtCore.Slot()
    def onChangeDialClicked(self):
        self.ui.horizontalSlider.setValue(self.ui.dial.value())
        self.ui.lcdNumber.display(self.ui.dial.value())

    @QtCore.Slot()
    def onCobmoBoxClicked(self):
        ...
    @QtCore.Slot()
    def onHorizontalSliderClicked(self):
        self.ui.dial.setValue(self.ui.horizontalSlider.value())
        self.ui.lcdNumber.display(self.ui.horizontalSlider.value())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
