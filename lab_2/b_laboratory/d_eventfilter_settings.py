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

        self.settings = QtCore.QSettings('lab2-d-settings')

        self.ui.comboBox.addItem('Decimal')
        self.ui.comboBox.addItem('Octal')
        self.ui.comboBox.addItem('Hex')
        self.ui.comboBox.addItem('Binary')

        self.loadData()

    def __initSignals(self):
        self.ui.dial.valueChanged.connect(self.onChangeDialClicked)
        self.ui.comboBox.textActivated.connect(self.onCobmoBoxClicked)
        self.ui.horizontalSlider.valueChanged.connect(self.onHorizontalSliderClicked)

    def loadData(self):
        self.ui.comboBox.setCurrentText(self.settings.value("combobox_state"))
        self.ui.lcdNumber.display(self.settings.value("lcdNumber_value"))
        self.ui.horizontalSlider.setValue(self.settings.value("horizontalslider_value"))
        self.ui.dial.setValue(self.settings.value("dial_value"))
        ...

    def keyPressEvent(self, event):
        if event.text() == "+" and self.ui.dial.value() in range(0, 99):
            self.ui.dial.setValue(self.ui.dial.value() + 1)
        elif event.text() == '-' and self.ui.dial.value() in range(1, 100):
            self.ui.dial.setValue(self.ui.dial.value() - 1)

    def closeEvent(self, event):
        self.settings.setValue("combobox_state", self.ui.comboBox.currentText())
        self.settings.setValue("lcdNumber_value", self.ui.lcdNumber.value())
        self.settings.setValue("dial_value", self.ui.dial.value())
        self.settings.setValue("horizontalslider_value", self.ui.horizontalSlider.value())

    def lcdView(self, numeral_sys):
        if numeral_sys == 'Octal':
            self.ui.lcdNumber.display(oct(self.ui.dial.value()))
        elif numeral_sys == 'Hex':
            self.ui.lcdNumber.display(hex(self.ui.dial.value()))
        elif numeral_sys == 'Binary':
            self.ui.lcdNumber.display(bin(self.ui.dial.value()))
        else:
            self.ui.lcdNumber.display(self.ui.dial.value())

    @QtCore.Slot()
    def onChangeDialClicked(self):
        self.ui.horizontalSlider.setValue(self.ui.dial.value())
        self.lcdView(self.ui.comboBox.currentText())
        # self.ui.lcdNumber.display(self.ui.dial.value())

    @QtCore.Slot()
    def onCobmoBoxClicked(self):
        if self.ui.comboBox.currentText() == 'Octal':
            self.ui.lcdNumber.display(oct(self.ui.dial.value()))
        elif self.ui.comboBox.currentText() == 'Hex':
            self.ui.lcdNumber.display(hex(self.ui.dial.value()))
        elif self.ui.comboBox.currentText() == 'Binary':
            self.ui.lcdNumber.display(bin(self.ui.dial.value()))
        elif self.ui.comboBox.currentText() == 'Decimal':
            self.ui.lcdNumber.display(self.ui.dial.value())
        ...

    @QtCore.Slot()
    def onHorizontalSliderClicked(self):
        self.ui.dial.setValue(self.ui.horizontalSlider.value())
        self.lcdView(self.ui.comboBox.currentText())
        # self.ui.lcdNumber.display(self.ui.horizontalSlider.value())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
