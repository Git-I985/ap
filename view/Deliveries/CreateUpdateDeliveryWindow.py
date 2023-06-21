from PyQt5 import QtWidgets, QtGui
from models import products_model, suppliers_model, delivery_status_model, delivery_model
from models.deliveries.delivery_to_products_model import DeliveryToProductsModel
from uic.delivery import Ui_MainWindow
from view.Deliveries.AddDeliveryItemWindow import AddDeliveryItemWindow
from orm import DeliveryToProduct


class CreateUpdateDeliveryWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.on_click)
        self.comboBox.setModel(suppliers_model)
        self.comboBox_2.setModel(delivery_status_model)

        self.update_index = None

        self.delivery_to_products_model = DeliveryToProductsModel()
        self.tableView.setModel(self.delivery_to_products_model)

        self.addDeliveryItemWindow = AddDeliveryItemWindow()

        self.pushButton_2.clicked.connect(lambda x: self.addDeliveryItemWindow.show())
        self.pushButton.clicked.connect(self.delete_delivery_item)
        self.addDeliveryItemWindow.pushButton.clicked.connect(self.on_delivery_item_add_click)

    def on_delivery_item_add_click(self):
        product_to_add = products_model.products[self.addDeliveryItemWindow.comboBox.currentIndex()]

        if not len(self.addDeliveryItemWindow.lineEdit.text()):
            return

        self.delivery_to_products_model.add_delivery_product(
            product_to_add,
            self.addDeliveryItemWindow.lineEdit.text())

        self.addDeliveryItemWindow.close()

    def delete_delivery_item(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        self.delivery_to_products_model.delete_product(indexes[0])

    def on_click(self):
        if self.update_index:
            self.update_delivery(self.update_index)
        else:
            self.create_delivery()

    def create_delivery(self):
        delivery_model.create_delivery(
            supplier=suppliers_model.suppliers[self.comboBox.currentIndex()],
            date=self.dateTimeEdit.dateTime().toPyDateTime(),
            status=delivery_status_model.delivery_statuses[self.comboBox_2.currentIndex()],
            products=self.delivery_to_products_model.products
        )
        self.close()

    def update_delivery(self, index):
        delivery = delivery_model.deliveries[index.row()]

        delivery_model.update_delivery(
            index,
            supplier=suppliers_model.suppliers[self.comboBox.currentIndex()],
            date=self.dateTimeEdit.dateTime().toPyDateTime(),
            status=delivery_status_model.delivery_statuses[self.comboBox_2.currentIndex()],
            products=self.delivery_to_products_model.products
        )

        self.close()
        self.update_index = None

    def load_delivery(self, index):
        self.update_index = index
        self.pushButton_3.setText('Изменить данные поставки')

        delivery = delivery_model.deliveries[index.row()]

        self.comboBox.setCurrentIndex(list(suppliers_model.suppliers).index(delivery.supplier))
        self.comboBox_2.setCurrentIndex(list(delivery_status_model.delivery_statuses).index(delivery.status))

        self.dateTimeEdit.setDateTime(delivery.date)

        delivery_products = DeliveryToProduct.select().where(DeliveryToProduct.delivery == delivery)

        for product in delivery_products:
            self.delivery_to_products_model.add_delivery_product(product.product, product.amount)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.pushButton_3.setText('Сохранить')
        self.delivery_to_products_model.clear()
