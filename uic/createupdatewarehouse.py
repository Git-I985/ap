# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/createupdatewarehouse.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateUpdateWarehouseWindow(object):
    def setupUi(self, CreateUpdateWarehouseWindow):
        CreateUpdateWarehouseWindow.setObjectName("CreateUpdateWarehouseWindow")
        CreateUpdateWarehouseWindow.resize(491, 264)
        self.centralwidget = QtWidgets.QWidget(CreateUpdateWarehouseWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        CreateUpdateWarehouseWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CreateUpdateWarehouseWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 491, 21))
        self.menubar.setObjectName("menubar")
        CreateUpdateWarehouseWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CreateUpdateWarehouseWindow)
        self.statusbar.setObjectName("statusbar")
        CreateUpdateWarehouseWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CreateUpdateWarehouseWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateUpdateWarehouseWindow)

    def retranslateUi(self, CreateUpdateWarehouseWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateUpdateWarehouseWindow.setWindowTitle(_translate("CreateUpdateWarehouseWindow", "Добавить / изменить товар на складе"))
        self.label.setText(_translate("CreateUpdateWarehouseWindow", "Товар"))
        self.label_2.setText(_translate("CreateUpdateWarehouseWindow", "Кол-во на складе"))
        self.pushButton.setText(_translate("CreateUpdateWarehouseWindow", "Сохранить"))
