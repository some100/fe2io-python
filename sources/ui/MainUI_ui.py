# Form implementation generated from reading ui file 'c:\Users\kris\Documents\GitHub\fe2io-python\sources\ui\MainUI.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 460)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\kris\\Documents\\GitHub\\fe2io-python\\sources\\ui\\resources/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setSizeGripEnabled(True)
        self.usernameLabel = QtWidgets.QLabel(parent=MainWindow)
        self.usernameLabel.setGeometry(QtCore.QRect(10, 145, 411, 20))
        self.usernameLabel.setObjectName("usernameLabel")
        self.lineEdit = QtWidgets.QLineEdit(parent=MainWindow)
        self.lineEdit.setGeometry(QtCore.QRect(10, 175, 311, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.connect_button = QtWidgets.QPushButton(parent=MainWindow)
        self.connect_button.setGeometry(QtCore.QRect(330, 175, 91, 21))
        self.connect_button.setObjectName("connect_button")
        self.status_label = QtWidgets.QLabel(parent=MainWindow)
        self.status_label.setGeometry(QtCore.QRect(10, 205, 331, 20))
        self.status_label.setObjectName("status_label")
        self.option_gb = QtWidgets.QGroupBox(parent=MainWindow)
        self.option_gb.setGeometry(QtCore.QRect(10, 235, 411, 211))
        self.option_gb.setObjectName("option_gb")
        self.volume_slider = QtWidgets.QSlider(parent=self.option_gb)
        self.volume_slider.setGeometry(QtCore.QRect(10, 41, 391, 21))
        self.volume_slider.setMaximum(100)
        self.volume_slider.setProperty("value", 70)
        self.volume_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.volume_slider.setObjectName("volume_slider")
        self.volume_label = QtWidgets.QLabel(parent=self.option_gb)
        self.volume_label.setGeometry(QtCore.QRect(10, 21, 391, 20))
        self.volume_label.setObjectName("volume_label")
        self.fade_box = QtWidgets.QCheckBox(parent=self.option_gb)
        self.fade_box.setGeometry(QtCore.QRect(10, 189, 201, 16))
        self.fade_box.setChecked(True)
        self.fade_box.setObjectName("fade_box")
        self.death_gb = QtWidgets.QGroupBox(parent=self.option_gb)
        self.death_gb.setGeometry(QtCore.QRect(9, 69, 391, 51))
        self.death_gb.setObjectName("death_gb")
        self.death_quiten = QtWidgets.QRadioButton(parent=self.death_gb)
        self.death_quiten.setGeometry(QtCore.QRect(8, 20, 71, 20))
        self.death_quiten.setChecked(True)
        self.death_quiten.setObjectName("death_quiten")
        self.death_stop = QtWidgets.QRadioButton(parent=self.death_gb)
        self.death_stop.setGeometry(QtCore.QRect(80, 20, 61, 20))
        self.death_stop.setObjectName("death_stop")
        self.death_nothing = QtWidgets.QRadioButton(parent=self.death_gb)
        self.death_nothing.setGeometry(QtCore.QRect(140, 20, 81, 20))
        self.death_nothing.setObjectName("death_nothing")
        self.leave_gb = QtWidgets.QGroupBox(parent=self.option_gb)
        self.leave_gb.setGeometry(QtCore.QRect(10, 130, 391, 51))
        self.leave_gb.setObjectName("leave_gb")
        self.leave_stop = QtWidgets.QRadioButton(parent=self.leave_gb)
        self.leave_stop.setGeometry(QtCore.QRect(7, 20, 61, 20))
        self.leave_stop.setChecked(True)
        self.leave_stop.setObjectName("leave_stop")
        self.leave_nothing = QtWidgets.QRadioButton(parent=self.leave_gb)
        self.leave_nothing.setGeometry(QtCore.QRect(70, 20, 81, 20))
        self.leave_nothing.setObjectName("leave_nothing")
        self.server_box = QtWidgets.QComboBox(parent=MainWindow)
        self.server_box.setGeometry(QtCore.QRect(330, 200, 91, 31))
        self.server_box.setObjectName("server_box")
        self.server_box.addItem("")
        self.server_box.addItem("")
        self.iconLabel = QtWidgets.QLabel(parent=MainWindow)
        self.iconLabel.setGeometry(QtCore.QRect(20, 20, 390, 110))
        self.iconLabel.setAutoFillBackground(False)
        self.iconLabel.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.iconLabel.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.iconLabel.setLineWidth(1)
        self.iconLabel.setText("")
        self.iconLabel.setScaledContents(False)
        self.iconLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.iconLabel.setObjectName("iconLabel")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FE2IO Python"))
        self.usernameLabel.setText(_translate("MainWindow", "Please Enter your Roblox Username:"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.status_label.setText(_translate("MainWindow", "Status: Disconnected"))
        self.option_gb.setTitle(_translate("MainWindow", "Options"))
        self.volume_label.setText(_translate("MainWindow", "Volume: %1%"))
        self.fade_box.setText(_translate("MainWindow", "Fade In / Out"))
        self.death_gb.setTitle(_translate("MainWindow", "On Death"))
        self.death_quiten.setText(_translate("MainWindow", "Quieten"))
        self.death_stop.setText(_translate("MainWindow", "Stop"))
        self.death_nothing.setText(_translate("MainWindow", "Nothing"))
        self.leave_gb.setTitle(_translate("MainWindow", "Leaving Game"))
        self.leave_stop.setText(_translate("MainWindow", "Stop"))
        self.leave_nothing.setText(_translate("MainWindow", "Nothing"))
        self.server_box.setItemText(0, _translate("MainWindow", "FE2.io"))
        self.server_box.setItemText(1, _translate("MainWindow", "LB\'s io"))
