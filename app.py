# процедуры и триггеры
# тесты
# скрины интерфейса
# панель администратора, для этого нужна авторизация

import sys

from PyQt5 import QtWidgets
from view.ClientsWindow import ClientsWindow
from view.ProductsWindow import ProductsWindow
from view.SuppliersWindow import SuppliersWindow
from view.UsersWindow import UsersWindow


# Trigger refresh.
# self.model.layoutChanged.emit()


class App(QtWidgets.QApplication):
    def __init__(self, *argv):
        super().__init__(*argv)

        self.productsWindow = ProductsWindow()
        self.suppliersWindow = SuppliersWindow()
        self.clientsWindow = ClientsWindow()
        self.usersWindow = UsersWindow()

        self.productsWindow.menubar.addAction(self.productsWindow.clients_action)
        self.productsWindow.menubar.addAction(self.productsWindow.suppliers_action)
        self.clientsWindow.menuBar.addAction(self.clientsWindow.products_action)
        self.clientsWindow.menuBar.addAction(self.clientsWindow.suppliers_action)
        self.suppliersWindow.menuBar.addAction(self.suppliersWindow.clients_action)
        self.suppliersWindow.menuBar.addAction(self.suppliersWindow.products_action)

        self.productsWindow.clients_action.triggered.connect(self.show_clients)
        self.productsWindow.suppliers_action.triggered.connect(self.show_suppliers)
        self.clientsWindow.products_action.triggered.connect(self.show_products)
        self.clientsWindow.suppliers_action.triggered.connect(self.show_suppliers)
        self.suppliersWindow.clients_action.triggered.connect(self.show_clients)
        self.suppliersWindow.products_action.triggered.connect(self.show_products)

        # self.productsWindow.show()
        self.usersWindow.show()

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


app = App(sys.argv)
app.exec()
