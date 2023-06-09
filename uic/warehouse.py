# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/warehouse.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WarehouseWindow(object):
    def setupUi(self, WarehouseWindow):
        WarehouseWindow.setObjectName("WarehouseWindow")
        WarehouseWindow.resize(547, 262)
        self.centralwidget = QtWidgets.QWidget(WarehouseWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        WarehouseWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WarehouseWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 547, 21))
        self.menubar.setObjectName("menubar")
        WarehouseWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WarehouseWindow)
        self.statusbar.setObjectName("statusbar")
        WarehouseWindow.setStatusBar(self.statusbar)
        self.clients_action = QtWidgets.QAction(WarehouseWindow)
        self.clients_action.setObjectName("clients_action")
        self.suppliers_action = QtWidgets.QAction(WarehouseWindow)
        self.suppliers_action.setObjectName("suppliers_action")
        self.products_action = QtWidgets.QAction(WarehouseWindow)
        self.products_action.setObjectName("products_action")
        self.orders_action = QtWidgets.QAction(WarehouseWindow)
        self.orders_action.setObjectName("orders_action")
        self.deliveries_action = QtWidgets.QAction(WarehouseWindow)
        self.deliveries_action.setObjectName("deliveries_action")
        self.warehouse_action = QtWidgets.QAction(WarehouseWindow)
        self.warehouse_action.setObjectName("warehouse_action")
        self.users_action = QtWidgets.QAction(WarehouseWindow)
        self.users_action.setObjectName("users_action")
        self.analytics_action = QtWidgets.QAction(WarehouseWindow)
        self.analytics_action.setObjectName("analytics_action")

        self.retranslateUi(WarehouseWindow)
        QtCore.QMetaObject.connectSlotsByName(WarehouseWindow)

    def retranslateUi(self, WarehouseWindow):
        _translate = QtCore.QCoreApplication.translate
        WarehouseWindow.setWindowTitle(_translate("WarehouseWindow", "Склад"))
        self.pushButton.setText(_translate("WarehouseWindow", "Найти товар на складе"))
        self.pushButton_4.setText(_translate("WarehouseWindow", "Удалить товар со склада"))
        self.pushButton_3.setText(_translate("WarehouseWindow", "Изменить товар на складе"))
        self.pushButton_2.setText(_translate("WarehouseWindow", "Добавить товар на склад"))
        self.clients_action.setText(_translate("WarehouseWindow", "Клиенты"))
        self.suppliers_action.setText(_translate("WarehouseWindow", "Поставщики"))
        self.products_action.setText(_translate("WarehouseWindow", "Продукты"))
        self.orders_action.setText(_translate("WarehouseWindow", "Заказы"))
        self.deliveries_action.setText(_translate("WarehouseWindow", "Поставки"))
        self.warehouse_action.setText(_translate("WarehouseWindow", "Склад"))
        self.users_action.setText(_translate("WarehouseWindow", "Пользователи"))
        self.analytics_action.setText(_translate("WarehouseWindow", "Аналитика"))
