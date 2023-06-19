from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from orm import Client


# Модель ClientsModel взаимодействует с источником данных, предоставляя интерфейс
# для других компонентов архитектуры. Способ обмена данными зависит от типа источника данных и способа реализации модели.
# Этот класс определяет интерфейс, который используется представлениями и делегатами для доступа к данным.
# Представления используют это соглашение для доступа к элементам данных в
# модели, но они не ограничены в способе представления этой информации пользователю.
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
