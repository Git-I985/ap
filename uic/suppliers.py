# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/suppliers.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Suppliers(object):
    def setupUi(self, Suppliers):
        Suppliers.setObjectName("Suppliers")
        Suppliers.resize(520, 240)
        self.centralwidget = QtWidgets.QWidget(Suppliers)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)
        Suppliers.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(Suppliers)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 520, 21))
        self.menuBar.setObjectName("menuBar")
        Suppliers.setMenuBar(self.menuBar)
        self.clients_action = QtWidgets.QAction(Suppliers)
        self.clients_action.setObjectName("clients_action")
        self.suppliers_action = QtWidgets.QAction(Suppliers)
        self.suppliers_action.setObjectName("suppliers_action")
        self.products_action = QtWidgets.QAction(Suppliers)
        self.products_action.setObjectName("products_action")
        self.warehouse_action = QtWidgets.QAction(Suppliers)
        self.warehouse_action.setObjectName("warehouse_action")

        self.retranslateUi(Suppliers)
        QtCore.QMetaObject.connectSlotsByName(Suppliers)

    def retranslateUi(self, Suppliers):
        _translate = QtCore.QCoreApplication.translate
        Suppliers.setWindowTitle(_translate("Suppliers", "Поставщики"))
        self.pushButton_2.setText(_translate("Suppliers", "Изменить данные поставщика"))
        self.pushButton_3.setText(_translate("Suppliers", "Удалить поставщика"))
        self.pushButton.setText(_translate("Suppliers", "Добавить поставщика"))
        self.pushButton_4.setText(_translate("Suppliers", "Найти"))
        self.clients_action.setText(_translate("Suppliers", "Клиенты"))
        self.suppliers_action.setText(_translate("Suppliers", "Поставщики"))
        self.products_action.setText(_translate("Suppliers", "Продукты"))
        self.warehouse_action.setText(_translate("Suppliers", "Склад"))
