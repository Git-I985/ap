from PyQt5 import QtWidgets, QtGui
from models import products_model, clients_model, order_status_model, orders_model
from models.orders.order_to_products_model import OrderToProductsModel
from uic.order import Ui_MainWindow
from view.Orders.AddOrderItemWindow import AddOrderItemWindow
from orm import OrderToProduct


class CreateUpdateOrdersWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_click)
        self.comboBox.setModel(clients_model)
        self.comboBox_2.setModel(order_status_model)

        self.update_index = None

        self.order_to_products_model = OrderToProductsModel()
        self.tableView.setModel(self.order_to_products_model)

        self.addOrderItemWindow = AddOrderItemWindow()

        self.pushButton_2.clicked.connect(lambda x: self.addOrderItemWindow.show())
        self.pushButton_3.clicked.connect(self.delete_order_item)
        self.addOrderItemWindow.pushButton.clicked.connect(self.on_order_item_add_click)

    def on_order_item_add_click(self):
        product_to_add = products_model.products[self.addOrderItemWindow.comboBox.currentIndex()]

        if not len(self.addOrderItemWindow.lineEdit.text()):
            return

        self.order_to_products_model.add_order_product(
            product_to_add,
            self.addOrderItemWindow.lineEdit.text())

        self.addOrderItemWindow.close()

    def delete_order_item(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        self.order_to_products_model.delete_product(indexes[0])

    def on_click(self):
        pass
        if self.update_index:
            self.update_order(self.update_index)
        else:
            self.create_order()

    def create_order(self):
        orders_model.create_order(
            client=clients_model.clients[self.comboBox.currentIndex()],
            delivery_date=self.dateTimeEdit.dateTime().toPyDateTime(),
            adress=self.lineEdit.text(),
            status=order_status_model.order_statuses[self.comboBox_2.currentIndex()],
            products=self.order_to_products_model.products
        )
        self.close()

    def update_order(self, index):
        order = orders_model.orders[index.row()]

        orders_model.update_order(
            index,
            client=clients_model.clients[self.comboBox.currentIndex()],
            delivery_date=self.dateTimeEdit.dateTime().toPyDateTime(),
            adress=self.lineEdit.text(),
            status=order_status_model.order_statuses[self.comboBox_2.currentIndex()],
            products=self.order_to_products_model.products
        )

        self.close()
        self.update_index = None

    def load_order(self, index):
        self.update_index = index
        self.pushButton.setText('Изменить данные заказа')

        order = orders_model.orders[index.row()]

        self.comboBox.setCurrentIndex(list(clients_model.clients).index(order.client))
        self.comboBox_2.setCurrentIndex(list(order_status_model.order_statuses).index(order.status))
        self.lineEdit.setText(str(order.adress))
        self.dateTimeEdit.setDateTime(order.delivery_date)

        order_products = OrderToProduct.select().where(OrderToProduct.order == order)
        for product in order_products:
            self.order_to_products_model.add_order_product(product.product, product.amount)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.lineEdit.clear()
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.pushButton.setText('Сохранить')
        self.order_to_products_model.clear()
