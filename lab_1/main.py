from PySide6 import QtWidgets, QtCore
# from ui.untitled import Ui_Form
# from ui.b_login import Ui_Form
# from ui.c_ship_parameters import Ui_Form
# from ui.d_engine_settings import Ui_Form
# from ui.e_profile_card import Ui_Form
# from ui.f_book_shop import Ui_Form
from ui.g_calculator import Ui_Form


from ui.a_add_ui_form import Ui_MainWindow


# pyside6-uic .\untitled.ui -o .\untitled.py

# app = QtWidgets.QApplication()
# window = QtWidgets.QWidget()
# window.setWindowTitle("Простейшее окно")
# window.show()

# app.exec()


# class Window(QtWidgets.QMainWindow):
class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        # self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.pushButtonLogin.setText("Логин")
        # self.ui.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    w = Window()
    w.show()

    app.exec()



