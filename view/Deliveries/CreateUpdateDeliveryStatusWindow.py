from PyQt5 import QtWidgets
from models import delivery_status_model
from uic.deliverystatus import Ui_MainWindow


class CreateUpdateDeliveryStatusWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.listView.setModel(delivery_status_model)
        self.pushButton_2.clicked.connect(self.add_status)
        self.pushButton.clicked.connect(self.delete_status)

    def add_status(self):
        status = self.lineEdit.text()
        if not len(status):
            return
        delivery_status_model.add_status(status)
        self.lineEdit.setText("")

    def delete_status(self):
        delivery_status_model.delete_status(self.listView.selectedIndexes()[0])
