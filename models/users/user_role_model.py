from PyQt5 import QtCore
from PyQt5.QtCore import Qt
# from peewee import fn
from orm import UserRole


class UsersRolesModel(QtCore.QAbstractTableModel):
    cols = [
        'название роли'
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.users_roles = []
        self.update()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            role = self.users_roles[index.row()]

            return [
                role.name
            ][index.column()]

    def update(self):
        self.users_roles = UserRole.select()
        self.layoutChanged.emit()

    def rowCount(self, index):
        return len(self.users_roles)

    def columnCount(self, index):
        return len(self.cols)

    def headerData(self, column, orientation, role=QtCore.Qt.DisplayRole):
        if not role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if orientation == QtCore.Qt.Horizontal:
            return QtCore.QVariant(self.cols[column])
