# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pid_controller.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.GraphWidget = QtWidgets.QWidget(self.centralwidget)
        self.GraphWidget.setGeometry(QtCore.QRect(25, 25, 500, 300))
        self.GraphWidget.setMinimumSize(QtCore.QSize(500, 300))
        self.GraphWidget.setMaximumSize(QtCore.QSize(500, 300))
        self.GraphWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.GraphWidget.setObjectName("GraphWidget")

        self.DeltaWidget = QtWidgets.QWidget(self.centralwidget)
        self.DeltaWidget.setGeometry(QtCore.QRect(370, 400, 350, 100))
        self.DeltaWidget.setMinimumSize(QtCore.QSize(350, 100))
        self.DeltaWidget.setMaximumSize(QtCore.QSize(350, 100))
        self.DeltaWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.DeltaWidget.setObjectName("DeltaWidget")

        self.label_delta_X = QtWidgets.QLabel(self.DeltaWidget)
        self.label_delta_X.setGeometry(QtCore.QRect(0, 0, 40, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_delta_X.setFont(font)
        self.label_delta_X.setObjectName("label_delta_X")

        self.delta_X_LCD = QtWidgets.QLCDNumber(self.DeltaWidget)
        self.delta_X_LCD.setGeometry(QtCore.QRect(50, 0, 100, 25))
        self.delta_X_LCD.setFrameShape(QtWidgets.QFrame.Box)
        self.delta_X_LCD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.delta_X_LCD.setDigitCount(10)
        self.delta_X_LCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.delta_X_LCD.setObjectName("delta_X_LCD")

        self.label_delta_Y = QtWidgets.QLabel(self.DeltaWidget)
        self.label_delta_Y.setGeometry(QtCore.QRect(200, 0, 40, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_delta_Y.setFont(font)
        self.label_delta_Y.setObjectName("label_delta_Y")

        self.delta_Y_LCD = QtWidgets.QLCDNumber(self.DeltaWidget)
        self.delta_Y_LCD.setGeometry(QtCore.QRect(250, 0, 100, 25))
        self.delta_Y_LCD.setFrameShape(QtWidgets.QFrame.Box)
        self.delta_Y_LCD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.delta_Y_LCD.setDigitCount(10)
        self.delta_Y_LCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.delta_Y_LCD.setObjectName("delta_Y_LCD")

        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(25, 350, 70, 30))
        self.clearButton.setObjectName("clearButton")
        self.clearButton.setText("ОЧИСТИТЬ")

        self.delta_X_button = QtWidgets.QPushButton(self.centralwidget)
        self.delta_X_button.setGeometry(QtCore.QRect(365, 350, 60, 30))
        self.delta_X_button.setObjectName("delta_X_button")
        self.delta_X_button.setStyleSheet("background-color: red")
        self.delta_X_button.setText("КУРСОР X")

        self.delta_Y_button = QtWidgets.QPushButton(self.centralwidget)
        self.delta_Y_button.setGeometry(QtCore.QRect(265, 350, 60, 30))
        self.delta_Y_button.setObjectName("delta_Y_button")
        self.delta_Y_button.setStyleSheet("background-color: red")
        self.delta_Y_button.setText("КУРСОР Y")

        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        self.help_button.setGeometry(QtCore.QRect(630, 500, 120, 60))
        self.help_button.setObjectName("help_button")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.help_button.setFont(font)
        self.help_button.setText("О ПРОГРАММЕ")

        self.setpoint_line = QtWidgets.QLineEdit(self.centralwidget)
        self.setpoint_line.setGeometry(QtCore.QRect(680, 50, 50, 25))
        self.setpoint_line.setMaxLength(6)
        self.setpoint_line.setObjectName("setpoint_line")
        self.P_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.P_edit.setGeometry(QtCore.QRect(680, 100, 50, 25))
        self.P_edit.setMaxLength(6)
        self.P_edit.setObjectName("P_edit")
        self.I_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.I_edit.setGeometry(QtCore.QRect(680, 150, 50, 25))
        self.I_edit.setMaxLength(6)
        self.I_edit.setObjectName("I_edit")
        self.D_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.D_edit.setGeometry(QtCore.QRect(680, 200, 50, 25))
        self.D_edit.setMaxLength(6)
        self.D_edit.setObjectName("D_edit")
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(630, 300, 100, 30))
        self.reset_button.setObjectName("reset_button")
        self.input_button = QtWidgets.QPushButton(self.centralwidget)
        self.input_button.setGeometry(QtCore.QRect(630, 250, 100, 30))
        self.input_button.setObjectName("input_button")
        self.start_stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_stop_button.setGeometry(QtCore.QRect(465, 350, 60, 30))
        self.start_stop_button.setObjectName("start_stop_button")
        self.meas_val = QtWidgets.QLCDNumber(self.centralwidget)
        self.meas_val.setGeometry(QtCore.QRect(180, 400, 125, 25))
        self.meas_val.setFrameShape(QtWidgets.QFrame.Box)
        self.meas_val.setFrameShadow(QtWidgets.QFrame.Plain)
        self.meas_val.setDigitCount(7)
        self.meas_val.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.meas_val.setObjectName("meas_val")
        self.err_val = QtWidgets.QLCDNumber(self.centralwidget)
        self.err_val.setGeometry(QtCore.QRect(180, 450, 125, 25))
        self.err_val.setFrameShape(QtWidgets.QFrame.Box)
        self.err_val.setFrameShadow(QtWidgets.QFrame.Plain)
        self.err_val.setDigitCount(7)
        self.err_val.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.err_val.setObjectName("err_val")
        self.label_SP = QtWidgets.QLabel(self.centralwidget)
        self.label_SP.setGeometry(QtCore.QRect(640, 50, 30, 25))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_SP.setFont(font)
        self.label_SP.setObjectName("label_SP")
        self.label_P = QtWidgets.QLabel(self.centralwidget)
        self.label_P.setGeometry(QtCore.QRect(640, 100, 30, 25))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_P.setFont(font)
        self.label_P.setObjectName("label_P")
        self.label_I = QtWidgets.QLabel(self.centralwidget)
        self.label_I.setGeometry(QtCore.QRect(640, 150, 30, 25))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_I.setFont(font)
        self.label_I.setObjectName("label_I")
        self.label_D = QtWidgets.QLabel(self.centralwidget)
        self.label_D.setGeometry(QtCore.QRect(640, 200, 30, 25))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_D.setFont(font)
        self.label_D.setObjectName("label_D")
        self.label_ms_val = QtWidgets.QLabel(self.centralwidget)
        self.label_ms_val.setGeometry(QtCore.QRect(25, 400, 130, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_ms_val.setFont(font)
        self.label_ms_val.setObjectName("label_ms_val")
        self.label_err_val = QtWidgets.QLabel(self.centralwidget)
        self.label_err_val.setGeometry(QtCore.QRect(25, 450, 130, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_err_val.setFont(font)
        self.label_err_val.setObjectName("label_err_val")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.label_P.setToolTip("<b>Пропорциональная составляющая</b> вырабатывает выходной сигнал, \
                                <br>противодействующий отклонению регулируемой величины от заданного значения, наблюдаемому в данный момент времени. Он тем больше, чем больше это отклонение.")
        self.label_D.setToolTip("<b>Дифференцирующая составляющая</b> пропорциональна темпу изменения отклонения регулируемой величины \
                                <br>и предназначена для противодействия отклонениям от целевого значения, которые прогнозируются в будущем.")
        self.label_I.setToolTip("<b>Интегрирующая составляющая</b> пропорциональна интегралу по времени от отклонения регулируемой величины. \
                                <br>Её используют для устранения статической ошибки. \
                                <br>Она позволяет регулятору со временем учесть статическую ошибку.")
        self.label_SP.setToolTip("<b>Заданное значение (уставка)</b>")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ПИД регулятор"))
        self.label_delta_X.setText(_translate("MainWindow", "|ΔX|"))
        self.label_delta_Y.setText(_translate("MainWindow", "|ΔY|"))
        self.input_button.setText(_translate("MainWindow", "ВВОД"))
        self.reset_button.setText(_translate("MainWindow", "СБРОС"))
        self.label_SP.setText(_translate("MainWindow", "SP"))
        self.label_P.setText(_translate("MainWindow", "P"))
        self.label_I.setText(_translate("MainWindow", "I"))
        self.label_D.setText(_translate("MainWindow", "D"))
        self.label_ms_val.setText(_translate("MainWindow", "Изм. значение"))
        self.label_err_val.setText(_translate("MainWindow", "Ошибка"))