from PyQt5 import QtWidgets
from models import delivery_model
from uic.deliveries import Ui_MainWindow
from view.Deliveries.CreateUpdateDeliveryWindow import CreateUpdateDeliveryWindow
from view.Deliveries.CreateUpdateDeliveryStatusWindow import CreateUpdateDeliveryStatusWindow


class DeliveriesWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.tableView.setModel(delivery_model)
        self.tableView.resizeColumnsToContents()

        self.createUpdateDeliveriesWindow = CreateUpdateDeliveryWindow()
        self.createUpdatedeliveriesStatusWindow = CreateUpdateDeliveryStatusWindow()

        self.pushButton.clicked.connect(lambda x: self.createUpdateDeliveriesWindow.show())
        self.pushButton_4.clicked.connect(lambda x: self.createUpdatedeliveriesStatusWindow.show())
        self.pushButton_3.clicked.connect(self.update_delivery)
        self.pushButton_2.clicked.connect(self.delete_delivery)

    def delete_delivery(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        delivery_model.delete_delivery(indexes[0])

    def update_delivery(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        self.createUpdateDeliveriesWindow.show()
        self.createUpdateDeliveriesWindow.load_delivery(indexes[0])
