import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from windows.products import Ui_MainWindow
from windows.updateproduct import Ui_CreateUpdateProductWIndow
from windows.updateproductcategories import Ui_UpdateProductsCategories
from windows.clients import Ui_Clients
from windows.suppliers import Ui_Suppliers
from windows.createupdatesupplier import Ui_CreateUpdateSupplier
from windows.createupdateclient import Ui_CreateUpdateClient
from models import Product, Warehouse, ProductCategory, Units, Client
from peewee import fn


# Trigger refresh.
# self.model.layoutChanged.emit()
class ProductsModel(QtCore.QAbstractTableModel):
    cols = [
        'название',
        'цена продажи',
        'цена закупки',
        'маржа %',
        'категория',
        'на складе',
        'ед-изм',
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.products = []
        self.update()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            product = self.products[index.row()]
            in_stock = Warehouse \
                .select(fn.SUM(Warehouse.amount)) \
                .where(Warehouse.product == product) \
                .scalar()

            return [
                product.name,
                str(product.sale_price) + 'Р',
                str(product.buy_price) + 'Р',
                str(product.margin) + '%',
                product.category.name,
                in_stock or 0,
                product.unit.name,
            ][index.column()]

    def update(self):
        self.products = Product.select()
        self.layoutChanged.emit()

    def rowCount(self, index):
        return len(self.products)

    def columnCount(self, index):
        return len(self.cols)

    def headerData(self, column, orientation, role=QtCore.Qt.DisplayRole):
        if not role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Horizontal:
            return QtCore.QVariant(self.cols[column])

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled

    def create_product(self,
                       name,
                       category,
                       sale_price,
                       buy_price,
                       unit,
                       margin):

        Product.create(
            name=name,
            category=category,
            sale_price=sale_price,
            buy_price=buy_price,
            unit=unit,
            margin=margin,
        )
        self.update()

    def delete_product(self, index):
        self.products[index.row()].delete_instance()
        self.update()

    def update_product(self,
                       index,
                       name,
                       category,
                       sale_price,
                       buy_price,
                       unit,
                       margin):
        product = self.products[index.row()]
        product.name = name
        product.category = category
        product.buy_price = buy_price
        product.sale_price = sale_price
        product.unit = unit
        product.margin = margin
        product.save()
        self.update()


class ClientsModel(QtCore.QAbstractTableModel):
    cols = [
        'Имя клиента / организации',
        'Адрес',
        'Телефон',
        'Email',
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clients = []
        self.update()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            client = self.clients[index.row()]
            return [
                client.company,
                client.adress,
                client.phone,
                client.mail
            ][index.column()]

    def update(self):
        self.clients = Client.select()
        self.layoutChanged.emit()

    def rowCount(self, index):
        return len(self.clients)

    def columnCount(self, index):
        return len(self.cols)

    def headerData(self, column, orientation, role=QtCore.Qt.DisplayRole):
        if not role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if orientation == QtCore.Qt.Horizontal:
            return QtCore.QVariant(self.cols[column])

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled

    def create_client(self,
                      company,
                      adress,
                      phone,
                      mail
                      ):
        Client.create(
            company=company,
            adress=adress,
            phone=phone,
            mail=mail,
        )
        self.update()

    def delete_client(self, index):
        self.clients[index.row()].delete_instance()
        self.update()

    def update_client(self, index,
                      company,
                      adress,
                      phone,
                      mail):
        client = self.clients[index.row()]
        client.company = company
        client.adress = adress
        client.phone = phone
        client.mail = mail
        client.save()
        self.update()


class ProductsCategoriesModel(QtCore.QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.product_categories = []
        self.update()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            category = self.product_categories[index.row()]
            return category.name

    def update(self):
        self.product_categories = ProductCategory.select()
        self.layoutChanged.emit()

    def add_category(self, category_name):
        ProductCategory.create(name=category_name)
        self.update()

    def delete_category(self, index):
        self.product_categories[index.row()].delete_instance()
        self.update()

    def rowCount(self, index):
        return len(self.product_categories)

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled


class ProductsUnitsModel(QtCore.QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.product_units = []
        self.update()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            unit = self.product_units[index.row()]
            return unit.name

    def update(self):
        self.product_units = Units.select()
        self.layoutChanged.emit()

    def add_unit(self, unit_name):
        Units.create(name=unit_name)
        self.update()

    def delete_product_unit(self, index):
        self.product_units[index.row()].delete_instance()
        self.update()

    def rowCount(self, index):
        return len(self.product_units)

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled


products_model = ProductsModel()
clients_model = ClientsModel()
units_model = ProductsUnitsModel()
product_categories_model = ProductsCategoriesModel()


class ProductsWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.tableView.setModel(products_model)
        self.tableView.resizeColumnsToContents()
        self.pushButton_3.clicked.connect(self.delete_product)
        self.createUpdateProductsWindow = UpdateProductsWindow()
        self.updateProductsCategoriesWindow = UpdateProductsCategoriesWindow()

        self.pushButton.clicked.connect(lambda x: self.createUpdateProductsWindow.show())
        self.pushButton_5.clicked.connect(lambda x: self.updateProductsCategoriesWindow.show())
        self.pushButton_4.clicked.connect(self.update_product)

    def delete_product(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        products_model.delete_product(indexes[0])

    def update_product(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        self.createUpdateProductsWindow.show()
        self.createUpdateProductsWindow.load_product(indexes[0])


class UpdateProductsWindow(QtWidgets.QMainWindow, Ui_CreateUpdateProductWIndow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_CreateUpdateProductWIndow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_click)
        self.comboBox.setModel(product_categories_model)
        self.comboBox_2.setModel(units_model)
        self.update_index = None

    def on_click(self):
        if self.update_index:
            self.update_product(self.update_index)
        else:
            self.create_product()

    def create_product(self):
        products_model.create_product(
            name=self.lineEdit.text(),
            category=product_categories_model.product_categories[self.comboBox.currentIndex()],
            buy_price=self.lineEdit_2.text(),
            sale_price=self.lineEdit_3.text(),
            unit=units_model.product_units[self.comboBox_2.currentIndex()],
            margin=self.lineEdit_4.text()
        )
        self.close()

    def update_product(self, index):
        products_model.update_product(
            index,
            name=self.lineEdit.text(),
            category=product_categories_model.product_categories[self.comboBox.currentIndex()],
            buy_price=self.lineEdit_2.text(),
            sale_price=self.lineEdit_3.text(),
            unit=units_model.product_units[self.comboBox_2.currentIndex()],
            margin=self.lineEdit_4.text()
        )
        self.close()
        self.update_index = None
        self.pushButton.setText('Сохранить')

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.lineEdit.clear()
        self.comboBox.setCurrentIndex(0)
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.comboBox_2.setCurrentIndex(0)
        self.lineEdit_4.clear()

    def load_product(self, index):
        self.update_index = index
        self.pushButton.setText('Обновить продукт')

        product = products_model.products[index.row()]
        self.lineEdit.setText(product.name)
        self.comboBox.setCurrentIndex(list(product_categories_model.product_categories).index(product.category))
        self.lineEdit_2.setText(str(product.buy_price))
        self.lineEdit_3.setText(str(product.sale_price))
        self.comboBox_2.setCurrentIndex(list(units_model.product_units).index(product.unit))
        self.lineEdit_4.setText(str(product.margin))
        pass


class UpdateProductsCategoriesWindow(QtWidgets.QMainWindow, Ui_UpdateProductsCategories):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_UpdateProductsCategories, self).__init__()
        self.setupUi(self)
        self.listView.setModel(product_categories_model)
        self.pushButton.clicked.connect(self.add_category)
        self.pushButton_2.clicked.connect(self.delete_category)

    def add_category(self):
        category = self.lineEdit.text()
        if not len(category):
            return
        product_categories_model.add_category(category)
        self.lineEdit.setText("")

    def update_category(self):
        # print(self.lineEdit.text)
        pass

    def delete_category(self):
        product_categories_model.delete_category(self.listView.selectedIndexes()[0])


class SuppliersWindow(QtWidgets.QMainWindow, Ui_Suppliers):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_Suppliers, self).__init__()
        self.setupUi(self)
        self.createUpdateSuppliersWindow = CreateUpdateSuppliersWindow()

        self.pushButton.clicked.connect(lambda x: self.createUpdateSuppliersWindow.show())


class ClientsWindow(QtWidgets.QMainWindow, Ui_Clients):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_Clients, self).__init__()
        self.setupUi(self)

        self.createUpdateClientWindow = CreateUpdateClientWindow()
        self.pushButton.clicked.connect(lambda x: self.createUpdateClientWindow.show())
        self.pushButton_2.clicked.connect(self.delete_client)
        self.pushButton_3.clicked.connect(self.update_client)
        self.tableView.setModel(clients_model)
        self.tableView.resizeColumnsToContents()

    def delete_client(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        clients_model.delete_client(indexes[0])

    def update_client(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        self.createUpdateClientWindow.show()
        self.createUpdateClientWindow.load_client(indexes[0])


class CreateUpdateClientWindow(QtWidgets.QMainWindow, Ui_CreateUpdateClient):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_CreateUpdateClient, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_click)
        self.update_index = None

    def on_click(self):
        if self.update_index:
            self.update_client(self.update_index)
        else:
            self.create_client()

    def create_client(self):
        clients_model.create_client(
            company=self.lineEdit.text(),
            adress=self.lineEdit_2.text(),
            phone=self.lineEdit_3.text(),
            mail=self.lineEdit_4.text()
        )
        self.close()

    def update_client(self, index):
        clients_model.update_client(
            index,
            company=self.lineEdit.text(),
            adress=self.lineEdit_2.text(),
            phone=self.lineEdit_3.text(),
            mail=self.lineEdit_4.text()
        )
        self.close()
        self.update_index = None
        self.pushButton.setText('Сохранить')

    def load_client(self, index):
        self.update_index = index
        self.pushButton.setText('Обновить клиента')

        client = clients_model.clients[index.row()]

        self.lineEdit.setText(client.company)
        self.lineEdit_2.setText(client.adress)
        self.lineEdit_3.setText(client.phone)
        self.lineEdit_4.setText(client.mail)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()


class CreateUpdateSuppliersWindow(QtWidgets.QMainWindow, Ui_CreateUpdateSupplier):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_CreateUpdateSupplier, self).__init__()
        self.setupUi(self)


class App(QtWidgets.QApplication):
    def __init__(self, *argv):
        super().__init__(*argv)

        self.productsWindow = ProductsWindow()
        self.suppliersWindow = SuppliersWindow()
        self.clientsWindow = ClientsWindow()

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

        self.productsWindow.show()

    def show_clients(self):
        self.clientsWindow.show()
        self.clientsWindow.activateWindow()

    def show_suppliers(self):
        self.suppliersWindow.show()
        self.suppliersWindow.activateWindow()

    def show_products(self):
        self.productsWindow.show()
        self.productsWindow.activateWindow()


app = App(sys.argv)
app.exec()
