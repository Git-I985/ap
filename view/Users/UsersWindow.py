from PyQt5 import QtWidgets
from models import users_model
from uic.users import Ui_MainWindow
from view.Users.CreateUpdateUserWindow import CreateUpdateUserWindow


class UsersWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.tableView.setModel(users_model)
        self.tableView.resizeColumnsToContents()

        self.createUpdateUserWindow = CreateUpdateUserWindow()
        self.pushButton_2.clicked.connect(lambda x: self.createUpdateUserWindow.show())
        self.pushButton.clicked.connect(self.delete_user)
        self.pushButton_3.clicked.connect(self.update_user)

    def delete_user(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        users_model.delete_user(indexes[0])

    def update_user(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        self.createUpdateUserWindow.show()
        self.createUpdateUserWindow.load_user(indexes[0])
