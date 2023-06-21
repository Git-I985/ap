from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from orm import DeliveryStatus


class DeliveryStatusModel(QtCore.QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.delivery_statuses = []
        self.update()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            status = self.delivery_statuses[index.row()]
            return status.name

    def update(self):
        self.delivery_statuses = DeliveryStatus.select()
        self.layoutChanged.emit()

    def add_status(self, status_name):
        DeliveryStatus.create(name=status_name)
        self.update()

    def delete_status(self, index):
        self.delivery_statuses[index.row()].delete_instance()
        self.update()

    def rowCount(self, index):
        return len(self.delivery_statuses)

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled
