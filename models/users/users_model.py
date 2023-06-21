from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from peewee import fn
from orm import User


class UsersModel(QtCore.QAbstractTableModel):
    cols = [
        'фио',
        'логин',
        'роль'
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.users = []
        self.update()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            user = self.users[index.row()]

            return [
                user.name,
                user.login,
                user.role.name
            ][index.column()]

    def update(self):
        self.users = User.select()
        self.layoutChanged.emit()

    def rowCount(self, index):
        return len(self.users)

    def columnCount(self, index):
        return len(self.cols)

    def headerData(self, column, orientation, role=QtCore.Qt.DisplayRole):
        if not role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if orientation == QtCore.Qt.Horizontal:
            return QtCore.QVariant(self.cols[column])

    def create_user(self,
                    login,
                    password,
                    role):

        User.create(
            login=login,
            password=password,
            role=role
        )
        self.update()

    def delete_user(self, index):
        self.users[index.row()].delete_instance()
        self.update()

    def update_user(self,
                    index,
                    login,
                    password,
                    role):
        user = self.users[index.row()]
        user.login = login
        user.password = password
        user.role = role
        user.save()
        self.update()
