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

        self.initLogin()

    def initLogin(self):
        if User.select().count() > 0:
            self.loginWindow = LoginWindow()
            self.loginWindow.show()
            self.loginWindow.pushButton.clicked.connect(self.login)
        else:
            self.productsWindow.show()

    def login(self):
        login = self.loginWindow.lineEdit.text()
        password = self.loginWindow.lineEdit_2.text()
        user = User.get_or_none(User.login == login, User.password == password)

        if user:
            self.loginWindow.close()
            self.productsWindow.show()
        else:
            QtWidgets.QMessageBox.critical(
                self.loginWindow,
                "Ошибка",
                "Пользователь не существует"
            )

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
