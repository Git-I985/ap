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
from view.Deliveries.DeliveriesWindow import DeliveriesWindow
from view.Analytics.AnalyticsWIndow import AnalyticsWindow
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
        self.deliveriesWindow = DeliveriesWindow()
        self.analyticsWindow = AnalyticsWindow()

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
            self.defaultWindow = self.analyticsWindow
        elif self.user.role.name == 'Менеджер':
            self.defaultWindow = self.ordersWindow
        elif self.user.role.name == 'Работник склада':
            self.defaultWindow = self.warehouseWindow
        elif self.user.role.name == 'Бухгалтер':
            self.defaultWindow = self.productsWindow

        self.defaultWindow.show()

    def setup_menubar_actions(self):
        if self.user.role.name == 'Администратор':
            # users menubar
            self.usersWindow.menubar.addAction(self.usersWindow.products_action)
            self.usersWindow.menubar.addAction(self.usersWindow.clients_action)
            self.usersWindow.menubar.addAction(self.usersWindow.suppliers_action)
            self.usersWindow.menubar.addAction(self.usersWindow.warehouse_action)
            self.usersWindow.menubar.addAction(self.usersWindow.orders_action)
            self.usersWindow.menubar.addAction(self.usersWindow.deliveries_action)
            self.usersWindow.menubar.addAction(self.usersWindow.users_action)
            self.usersWindow.menubar.addAction(self.usersWindow.analytics_action)

            # products menubar
            self.productsWindow.menubar.addAction(self.productsWindow.clients_action)
            self.productsWindow.menubar.addAction(self.productsWindow.suppliers_action)
            self.productsWindow.menubar.addAction(self.productsWindow.warehouse_action)
            self.productsWindow.menubar.addAction(self.productsWindow.orders_action)
            self.productsWindow.menubar.addAction(self.productsWindow.deliveries_action)
            self.productsWindow.menubar.addAction(self.productsWindow.products_action)
            self.productsWindow.menubar.addAction(self.productsWindow.users_action)
            self.productsWindow.menubar.addAction(self.productsWindow.analytics_action)

            # clients menubar
            self.clientsWindow.menuBar.addAction(self.clientsWindow.products_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.suppliers_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.warehouse_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.orders_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.deliveries_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.clients_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.users_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.analytics_action)

            # suppliers menubar
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.clients_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.products_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.warehouse_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.orders_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.deliveries_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.suppliers_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.users_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.analytics_action)

            # warehouse menubar
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.products_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.clients_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.suppliers_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.orders_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.deliveries_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.warehouse_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.users_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.analytics_action)

            # orders menubar
            self.ordersWindow.menubar.addAction(self.ordersWindow.products_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.clients_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.suppliers_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.warehouse_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.deliveries_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.orders_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.users_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.analytics_action)

            # deliveries menubar
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.products_action)
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.clients_action)
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.suppliers_action)
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.warehouse_action)
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.orders_action)
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.deliveries_action)
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.users_action)
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.analytics_action)

            # analytics menubar
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.products_action)
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.clients_action)
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.suppliers_action)
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.warehouse_action)
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.orders_action)
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.deliveries_action)
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.users_action)
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.analytics_action)


        elif self.user.role.name == 'Менеджер':
            # products menubar
            self.productsWindow.menubar.addAction(self.productsWindow.clients_action)
            self.productsWindow.menubar.addAction(self.productsWindow.suppliers_action)
            self.productsWindow.menubar.addAction(self.productsWindow.warehouse_action)
            self.productsWindow.menubar.addAction(self.productsWindow.orders_action)
            self.productsWindow.menubar.addAction(self.productsWindow.deliveries_action)
            self.productsWindow.menubar.addAction(self.productsWindow.products_action)
            self.productsWindow.menubar.addAction(self.productsWindow.analytics_action)

            # clients menubar
            self.clientsWindow.menuBar.addAction(self.clientsWindow.products_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.suppliers_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.warehouse_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.orders_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.deliveries_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.clients_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.analytics_action)

            # suppliers menubar
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.clients_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.products_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.warehouse_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.orders_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.deliveries_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.suppliers_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.analytics_action)

            # warehouse menubar
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.products_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.clients_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.suppliers_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.orders_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.deliveries_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.warehouse_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.analytics_action)

            # orders menubar
            self.ordersWindow.menubar.addAction(self.ordersWindow.products_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.clients_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.suppliers_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.warehouse_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.deliveries_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.orders_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.analytics_action)

            # deliveries menubar
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.products_action)
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.clients_action)
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.suppliers_action)
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.warehouse_action)
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.orders_action)
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.deliveries_action)
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.analytics_action)

            # analytics menubar
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.products_action)
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.clients_action)
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.suppliers_action)
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.warehouse_action)
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.orders_action)
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.deliveries_action)
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.analytics_action)

        elif self.user.role.name == 'Работник склада':
            # warehouse menubar
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.deliveries_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.warehouse_action)

            # deliveries menubar
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.warehouse_action)
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.deliveries_action)

        elif self.user.role.name == 'Бухгалтер':
            # products menubar
            self.productsWindow.menubar.addAction(self.productsWindow.clients_action)
            self.productsWindow.menubar.addAction(self.productsWindow.suppliers_action)
            self.productsWindow.menubar.addAction(self.productsWindow.warehouse_action)
            self.productsWindow.menubar.addAction(self.productsWindow.orders_action)
            self.productsWindow.menubar.addAction(self.productsWindow.deliveries_action)
            self.productsWindow.menubar.addAction(self.productsWindow.products_action)
            self.productsWindow.menubar.addAction(self.productsWindow.analytics_action)

            # clients menubar
            self.clientsWindow.menuBar.addAction(self.clientsWindow.products_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.suppliers_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.warehouse_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.orders_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.deliveries_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.clients_action)
            self.clientsWindow.menuBar.addAction(self.clientsWindow.analytics_action)

            # suppliers menubar
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.clients_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.products_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.warehouse_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.orders_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.deliveries_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.suppliers_action)
            self.suppliersWindow.menuBar.addAction(self.suppliersWindow.analytics_action)

            # warehouse menubar
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.products_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.clients_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.suppliers_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.orders_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.deliveries_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.warehouse_action)
            self.warehouseWindow.menubar.addAction(self.warehouseWindow.analytics_action)

            # orders menubar
            self.ordersWindow.menubar.addAction(self.ordersWindow.products_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.clients_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.suppliers_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.warehouse_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.deliveries_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.orders_action)
            self.ordersWindow.menubar.addAction(self.ordersWindow.analytics_action)

            # deliveries menubar
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.products_action)
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.clients_action)
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.suppliers_action)
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.warehouse_action)
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.orders_action)
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.deliveries_action)
            self.deliveriesWindow.menuBar.addAction(self.deliveriesWindow.analytics_action)

            # analytics menubar
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.products_action)
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.clients_action)
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.suppliers_action)
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.warehouse_action)
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.orders_action)
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.deliveries_action)
            self.analyticsWindow.menubar.addAction(self.analyticsWindow.analytics_action)

        # users window actions
        self.usersWindow.warehouse_action.triggered.connect(self.show_warehouse)
        self.usersWindow.suppliers_action.triggered.connect(self.show_suppliers)
        self.usersWindow.clients_action.triggered.connect(self.show_clients)
        self.usersWindow.orders_action.triggered.connect(self.show_orders)
        self.usersWindow.deliveries_action.triggered.connect(self.show_deliveries)
        self.usersWindow.products_action.triggered.connect(self.show_products)
        self.usersWindow.users_action.triggered.connect(self.show_users)
        self.usersWindow.analytics_action.triggered.connect(self.show_analytics)

        # products window actions
        self.productsWindow.warehouse_action.triggered.connect(self.show_warehouse)
        self.productsWindow.suppliers_action.triggered.connect(self.show_suppliers)
        self.productsWindow.clients_action.triggered.connect(self.show_clients)
        self.productsWindow.orders_action.triggered.connect(self.show_orders)
        self.productsWindow.deliveries_action.triggered.connect(self.show_deliveries)
        self.productsWindow.products_action.triggered.connect(self.show_products)
        self.productsWindow.users_action.triggered.connect(self.show_users)
        self.productsWindow.analytics_action.triggered.connect(self.show_analytics)

        # clients window actions
        self.clientsWindow.products_action.triggered.connect(self.show_products)
        self.clientsWindow.warehouse_action.triggered.connect(self.show_warehouse)
        self.clientsWindow.suppliers_action.triggered.connect(self.show_suppliers)
        self.clientsWindow.orders_action.triggered.connect(self.show_orders)
        self.clientsWindow.deliveries_action.triggered.connect(self.show_deliveries)
        self.clientsWindow.clients_action.triggered.connect(self.show_clients)
        self.clientsWindow.users_action.triggered.connect(self.show_users)
        self.clientsWindow.analytics_action.triggered.connect(self.show_analytics)

        # suppliers window actions
        self.suppliersWindow.clients_action.triggered.connect(self.show_clients)
        self.suppliersWindow.products_action.triggered.connect(self.show_products)
        self.suppliersWindow.warehouse_action.triggered.connect(self.show_warehouse)
        self.suppliersWindow.orders_action.triggered.connect(self.show_orders)
        self.suppliersWindow.deliveries_action.triggered.connect(self.show_deliveries)
        self.suppliersWindow.suppliers_action.triggered.connect(self.show_suppliers)
        self.suppliersWindow.users_action.triggered.connect(self.show_users)
        self.suppliersWindow.analytics_action.triggered.connect(self.show_analytics)

        # warehouse window actions
        self.warehouseWindow.clients_action.triggered.connect(self.show_clients)
        self.warehouseWindow.products_action.triggered.connect(self.show_products)
        self.warehouseWindow.suppliers_action.triggered.connect(self.show_suppliers)
        self.warehouseWindow.orders_action.triggered.connect(self.show_orders)
        self.warehouseWindow.deliveries_action.triggered.connect(self.show_deliveries)
        self.warehouseWindow.warehouse_action.triggered.connect(self.show_warehouse)
        self.warehouseWindow.users_action.triggered.connect(self.show_users)
        self.warehouseWindow.analytics_action.triggered.connect(self.show_analytics)

        # orders window actions
        self.ordersWindow.clients_action.triggered.connect(self.show_clients)
        self.ordersWindow.products_action.triggered.connect(self.show_products)
        self.ordersWindow.suppliers_action.triggered.connect(self.show_suppliers)
        self.ordersWindow.warehouse_action.triggered.connect(self.show_warehouse)
        self.ordersWindow.deliveries_action.triggered.connect(self.show_deliveries)
        self.ordersWindow.orders_action.triggered.connect(self.show_orders)
        self.ordersWindow.users_action.triggered.connect(self.show_users)
        self.ordersWindow.analytics_action.triggered.connect(self.show_analytics)

        # deliveries window actions
        self.deliveriesWindow.clients_action.triggered.connect(self.show_clients)
        self.deliveriesWindow.products_action.triggered.connect(self.show_products)
        self.deliveriesWindow.suppliers_action.triggered.connect(self.show_suppliers)
        self.deliveriesWindow.warehouse_action.triggered.connect(self.show_warehouse)
        self.deliveriesWindow.orders_action.triggered.connect(self.show_orders)
        self.deliveriesWindow.deliveries_action.triggered.connect(self.show_deliveries)
        self.deliveriesWindow.users_action.triggered.connect(self.show_users)
        self.deliveriesWindow.analytics_action.triggered.connect(self.show_analytics)

        # analytics window actions
        self.analyticsWindow.clients_action.triggered.connect(self.show_clients)
        self.analyticsWindow.products_action.triggered.connect(self.show_products)
        self.analyticsWindow.suppliers_action.triggered.connect(self.show_suppliers)
        self.analyticsWindow.warehouse_action.triggered.connect(self.show_warehouse)
        self.analyticsWindow.orders_action.triggered.connect(self.show_orders)
        self.analyticsWindow.deliveries_action.triggered.connect(self.show_deliveries)
        self.analyticsWindow.users_action.triggered.connect(self.show_users)
        self.analyticsWindow.analytics_action.triggered.connect(self.show_analytics)

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

    def show_deliveries(self):
        self.deliveriesWindow.show()
        self.deliveriesWindow.activateWindow()

    def show_analytics(self):
        self.analyticsWindow.show()
        self.analyticsWindow.activateWindow()


app = App(sys.argv)
app.exec()
