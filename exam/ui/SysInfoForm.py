# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SysInfoForm.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(825, 712)
        Form.setMinimumSize(QSize(750, 650))
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_1SysInfo = QWidget()
        self.tab_1SysInfo.setObjectName(u"tab_1SysInfo")
        self.layoutWidget = QWidget(self.tab_1SysInfo)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 682, 500))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.delayTimeLineEdit = QLineEdit(self.layoutWidget)
        self.delayTimeLineEdit.setObjectName(u"delayTimeLineEdit")
        self.delayTimeLineEdit.setMinimumSize(QSize(270, 20))

        self.verticalLayout_3.addWidget(self.delayTimeLineEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CpuInfoLabel = QLabel(self.layoutWidget)
        self.CpuInfoLabel.setObjectName(u"CpuInfoLabel")
        self.CpuInfoLabel.setMinimumSize(QSize(100, 21))

        self.verticalLayout.addWidget(self.CpuInfoLabel)

        self.CpuCoresLabel = QLabel(self.layoutWidget)
        self.CpuCoresLabel.setObjectName(u"CpuCoresLabel")
        self.CpuCoresLabel.setMinimumSize(QSize(100, 21))

        self.verticalLayout.addWidget(self.CpuCoresLabel)

        self.CpuUsageLabel = QLabel(self.layoutWidget)
        self.CpuUsageLabel.setObjectName(u"CpuUsageLabel")
        self.CpuUsageLabel.setMinimumSize(QSize(100, 21))

        self.verticalLayout.addWidget(self.CpuUsageLabel)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.TotalRamLabel = QLabel(self.layoutWidget)
        self.TotalRamLabel.setObjectName(u"TotalRamLabel")
        self.TotalRamLabel.setMinimumSize(QSize(100, 21))

        self.verticalLayout_2.addWidget(self.TotalRamLabel)

        self.RamUsageLabel = QLabel(self.layoutWidget)
        self.RamUsageLabel.setObjectName(u"RamUsageLabel")
        self.RamUsageLabel.setMinimumSize(QSize(100, 21))

        self.verticalLayout_2.addWidget(self.RamUsageLabel)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.HddInfoLabel = QLabel(self.layoutWidget)
        self.HddInfoLabel.setObjectName(u"HddInfoLabel")
        self.HddInfoLabel.setMinimumSize(QSize(170, 21))

        self.verticalLayout_3.addWidget(self.HddInfoLabel)

        self.HddInfoBoxplainTextEdit = QPlainTextEdit(self.layoutWidget)
        self.HddInfoBoxplainTextEdit.setObjectName(u"HddInfoBoxplainTextEdit")
        self.HddInfoBoxplainTextEdit.setMinimumSize(QSize(680, 360))
        self.HddInfoBoxplainTextEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.HddInfoBoxplainTextEdit)

        self.tabWidget.addTab(self.tab_1SysInfo, "")
        self.tab_2WinProcesses = QWidget()
        self.tab_2WinProcesses.setObjectName(u"tab_2WinProcesses")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2WinProcesses)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.WinProcessesPlainTextEdit = QPlainTextEdit(self.tab_2WinProcesses)
        self.WinProcessesPlainTextEdit.setObjectName(u"WinProcessesPlainTextEdit")
        self.WinProcessesPlainTextEdit.setMinimumSize(QSize(710, 590))

        self.verticalLayout_4.addWidget(self.WinProcessesPlainTextEdit)

        self.tabWidget.addTab(self.tab_2WinProcesses, "")
        self.tab_3WinServices = QWidget()
        self.tab_3WinServices.setObjectName(u"tab_3WinServices")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3WinServices)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.WinServicesPlainTextEdit = QPlainTextEdit(self.tab_3WinServices)
        self.WinServicesPlainTextEdit.setObjectName(u"WinServicesPlainTextEdit")
        self.WinServicesPlainTextEdit.setMinimumSize(QSize(710, 590))

        self.verticalLayout_5.addWidget(self.WinServicesPlainTextEdit)

        self.tabWidget.addTab(self.tab_3WinServices, "")
        self.tab_4WinSheduler = QWidget()
        self.tab_4WinSheduler.setObjectName(u"tab_4WinSheduler")
        self.verticalLayout_6 = QVBoxLayout(self.tab_4WinSheduler)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.WinShedulePlainTextEdit = QPlainTextEdit(self.tab_4WinSheduler)
        self.WinShedulePlainTextEdit.setObjectName(u"WinShedulePlainTextEdit")
        self.WinShedulePlainTextEdit.setMinimumSize(QSize(710, 590))

        self.verticalLayout_6.addWidget(self.WinShedulePlainTextEdit)

        self.tabWidget.addTab(self.tab_4WinSheduler, "")

        self.horizontalLayout_3.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"KhakhulinExamSysInfo", None))
        self.delayTimeLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0432\u0440\u0435\u043c\u044f \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0438 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438", None))
        self.CpuInfoLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.CpuCoresLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.CpuUsageLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.TotalRamLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.RamUsageLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.HddInfoLabel.setText(QCoreApplication.translate("Form", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0436\u0451\u0441\u0442\u043a\u0438\u0445 \u0434\u0438\u0441\u043a\u0430\u0445:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1SysInfo), QCoreApplication.translate("Form", u"\u041e\u0431\u0449\u0438\u0435 \u0441\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u043e \u0441\u0438\u0441\u0442\u0435\u043c\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2WinProcesses), QCoreApplication.translate("Form", u"\u0420\u0430\u0431\u043e\u0442\u0430\u044e\u0449\u0438\u0435 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3WinServices), QCoreApplication.translate("Form", u"\u0420\u0430\u0431\u043e\u0442\u0430\u044e\u0449\u0438\u0435 \u0441\u043b\u0443\u0436\u0431\u044b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4WinSheduler), QCoreApplication.translate("Form", u"\u0417\u0430\u0434\u0430\u0447\u0438 (\u0438\u0437 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0449\u0438\u043a\u0430 \u0437\u0430\u0434\u0430\u0447)", None))
    # retranslateUi

