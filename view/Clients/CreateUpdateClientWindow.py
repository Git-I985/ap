from PyQt5 import QtWidgets, QtGui
from models import clients_model
from uic.createupdateclient import Ui_CreateUpdateClient


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

    def load_client(self, index):
        self.update_index = index
        self.pushButton.setText('Изменить данные клиента')
        self.setWindowTitle('Изменить данные клиента')

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
        self.pushButton.setText('Сохранить')
        self.setWindowTitle('Добавить клиента')
