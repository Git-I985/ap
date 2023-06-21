from PyQt5 import QtWidgets
from models import orders_model
from uic.orders import Ui_MainWindow
from view.Orders.CreateUpdateOrdersWindow import CreateUpdateOrdersWindow
from view.Orders.CreateUpdateOrderStatusWindow import CreateUpdateOrderStatusWindow


class OrdersWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.tableView.setModel(orders_model)
        self.tableView.resizeColumnsToContents()

        self.createUpdateOrdersWindow = CreateUpdateOrdersWindow()
        self.createUpdateOrderStatusWindow = CreateUpdateOrderStatusWindow()

        self.pushButton_2.clicked.connect(lambda x: self.createUpdateOrdersWindow.show())
        self.pushButton_5.clicked.connect(lambda x: self.createUpdateOrderStatusWindow.show())
        self.pushButton_4.clicked.connect(self.update_order)
        self.pushButton_3.clicked.connect(self.delete_order)

    def delete_order(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        orders_model.delete_order(indexes[0])

    def update_order(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        self.createUpdateOrdersWindow.show()
        self.createUpdateOrdersWindow.load_order(indexes[0])
