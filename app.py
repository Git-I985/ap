# процедуры и триггеры
# тесты
# скрины интерфейса
# панель администратора, для этого нужна авторизация

import sys

from PyQt5 import QtWidgets
from orm import User
from view.Clients.ClientsWindow import ClientsWindow
from view.Products.ProductsWindow import ProductsWindow
from view.Suppliers.SuppliersWindow import SuppliersWindow
from view.Users.UsersWindow import UsersWindow
from view.LoginWindow import LoginWindow
from view.Warehouse.WarehouseWindow import WarehouseWindow
from view.Orders.OrdersWindow import OrdersWindow
from utils import hash_password


# Trigger refresh.
# self.model.layoutChanged.emit()


class App(QtWidgets.QApplication):
    def __init__(self, *argv):
        super().__init__(*argv)

        self.productsWindow = ProductsWindow()
        self.suppliersWindow = SuppliersWindow()
        self.clientsWindow = ClientsWindow()
        self.usersWindow = UsersWindow()
        self.warehouseWindow = WarehouseWindow()
        self.ordersWindow = OrdersWindow()

        self.init_login()

    def init_login(self):
        if User.select().count() > 0:
            self.loginWindow = LoginWindow()
            self.loginWindow.show()
            self.loginWindow.pushButton.clicked.connect(self.login)
        else:
            self.defaultWindow = self.usersWindow
            self.defaultWindow.show()

    def login(self):
        login = self.loginWindow.lineEdit.text()
        password = hash_password(self.loginWindow.lineEdit_2.text())
        # FIXME remove
        # login = 'admin'
        # password = hash_password('admin')
        user = User.get_or_none(User.login == login, User.password == password)

        if user:
            self.loginWindow.close()
            self.user = user

            self.setup_default_window()
            self.setup_menubar_actions()
        else:
            QtWidgets.QMessageBox.critical(
                self.loginWindow,
                "Ошибка",
                "Пользователь не существует"
            )

    def setup_default_window(self):
        if self.user.role.name == 'Администратор':
            self.defaultWindow = self.clientsWindow
        elif self.user.role.name == 'Менеджер':
            self.defaultWindow = self.productsWindow
        elif self.user.role.name == 'Работник склада':
            self.defaultWindow = self.productsWindow
        elif self.user.role.name == 'Бухгалтер':
            self.defaultWindow = self.productsWindow

        self.defaultWindow.show()

    def setup_menubar_actions(self):
        if self.user.role.name == 'Администратор':
            pass

        elif self.user.role.name == 'Менеджер':
            # products menubar
            self.productsWindow.menubar.addAction(self.productsWindow.clients_action)
            self.productsWindow.menubar.addAction(self.productsWindow.suppliers_action)
            self.productsWindow.menubar.addAction(self.productsWindow.warehouse_action)
            self.productsWindow.menubar.addAction(self.productsWindow.orders_action)

            # clients menubar
            self.clientsWindow.menuBar.addAction(self.clientsWindow.products_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.suppliers_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.warehouse_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.orders_action)

            # suppliers menubar
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.clients_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.products_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.warehouse_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.orders_action)

            # warehouse menubar
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.products_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.clients_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.suppliers_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.orders_action)

            # users menubar
            self.usersWindow.menubar.addAction(self.usersWindow.products_action)
            self.usersWindow.menubar.addAction(self.usersWindow.clients_action)
            self.usersWindow.menubar.addAction(self.usersWindow.suppliers_action)
            self.usersWindow.menubar.addAction(self.usersWindow.warehouse_action)
            self.usersWindow.menubar.addAction(self.usersWindow.orders_action)

            # orders menubar
            self.ordersWindow.menubar.addAction(self.ordersWindow.products_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.clients_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.suppliers_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.warehouse_action)

        elif self.user.role.name == 'Работник склада':
            pass

        elif self.user.role.name == 'Бухгалтер':
            pass

        # products window actions
        self.productsWindow.warehouse_action.triggered.connect(self.show_warehouse)
        self.productsWindow.suppliers_action.triggered.connect(self.show_suppliers)
        self.productsWindow.clients_action.triggered.connect(self.show_clients)
        self.productsWindow.orders_action.triggered.connect(self.show_orders)

        # clients window actions
        self.clientsWindow.products_action.triggered.connect(self.show_products)
        self.clientsWindow.warehouse_action.triggered.connect(self.show_warehouse)
        self.clientsWindow.suppliers_action.triggered.connect(self.show_suppliers)
        self.clientsWindow.orders_action.triggered.connect(self.show_orders)

        # suppliers window actions
        self.suppliersWindow.clients_action.triggered.connect(self.show_clients)
        self.suppliersWindow.products_action.triggered.connect(self.show_products)
        self.suppliersWindow.warehouse_action.triggered.connect(self.show_warehouse)
        self.suppliersWindow.orders_action.triggered.connect(self.show_orders)

        # warehouse window actions
        self.warehouseWindow.clients_action.triggered.connect(self.show_clients)
        self.warehouseWindow.products_action.triggered.connect(self.show_products)
        self.warehouseWindow.suppliers_action.triggered.connect(self.show_suppliers)
        self.warehouseWindow.orders_action.triggered.connect(self.show_orders)

        # orders window actions
        self.ordersWindow.clients_action.triggered.connect(self.show_clients)
        self.ordersWindow.products_action.triggered.connect(self.show_products)
        self.ordersWindow.suppliers_action.triggered.connect(self.show_suppliers)
        self.ordersWindow.suppliers_action.triggered.connect(self.show_warehouse)

    def show_clients(self):
        self.clientsWindow.show()
        self.clientsWindow.activateWindow()

    def show_suppliers(self):
        self.suppliersWindow.show()
        self.suppliersWindow.activateWindow()

    def show_products(self):
        self.productsWindow.show()
        self.productsWindow.activateWindow()

    def show_users(self):
        self.usersWindow.show()
        self.usersWindow.activateWindow()

    def show_warehouse(self):
        self.warehouseWindow.show()
        self.warehouseWindow.activateWindow()

    def show_orders(self):
        self.ordersWindow.show()
        self.ordersWindow.activateWindow()


app = App(sys.argv)
app.exec()
