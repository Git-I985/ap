from PyQt5 import QtWidgets
from models import order_status_model
from uic.orderstatus import Ui_MainWindow


class CreateUpdateOrderStatusWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.listView.setModel(order_status_model)
        self.pushButton.clicked.connect(self.add_status)
        self.pushButton_2.clicked.connect(self.delete_status)

    def add_status(self):
        status = self.lineEdit.text()
        if not len(status):
            return
        order_status_model.add_status(status)
        self.lineEdit.setText("")

    def delete_status(self):
        order_status_model.delete_status(self.listView.selectedIndexes()[0])
