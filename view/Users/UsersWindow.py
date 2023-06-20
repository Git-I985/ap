from PyQt5 import QtWidgets
from models import users_model
from uic.users import Ui_MainWindow


class UsersWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.tableView.setModel(users_model)
        self.tableView.resizeColumnsToContents()

        # self.createUpdateClientWindow = CreateUpdateClientWindow()
        # self.pushButton.clicked.connect(lambda x: self.createUpdateClientWindow.show())
        # self.pushButton_2.clicked.connect(self.delete_client)
        # self.pushButton_3.clicked.connect(self.update_client)
        # self.tableView.resizeColumnsToContents()
