from PyQt5 import QtWidgets
from models import clients_model
from view.CreateUpdateClientWindow import CreateUpdateClientWindow
from uic.clients import Ui_Clients


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
