from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from orm import Supplier


class SuppliersModel(QtCore.QAbstractTableModel):
    cols = [
        'Имя клиента / организации',
        'Адрес',
        'Телефон',
        'Email',
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.suppliers = []
        self.update()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            supplier = self.suppliers[index.row()]
            return [
                supplier.company,
                supplier.adress,
                supplier.phone,
                supplier.mail
            ][index.column()]

    def update(self):
        self.suppliers = Supplier.select()
        self.layoutChanged.emit()

    def rowCount(self, index):
        return len(self.suppliers)

    def columnCount(self, index):
        return len(self.cols)

    def headerData(self, column, orientation, role=QtCore.Qt.DisplayRole):
        if not role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if orientation == QtCore.Qt.Horizontal:
            return QtCore.QVariant(self.cols[column])

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled

    def create_supplier(self,
                        company,
                        adress,
                        phone,
                        mail
                        ):
        Supplier.create(
            company=company,
            adress=adress,
            phone=phone,
            mail=mail,
        )
        self.update()

    def delete_supplier(self, index):
        self.suppliers[index.row()].delete_instance()
        self.update()

    def update_supplier(self, index,
                        company,
                        adress,
                        phone,
                        mail):
        supplier = self.suppliers[index.row()]
        supplier.company = company
        supplier.adress = adress
        supplier.phone = phone
        supplier.mail = mail
        supplier.save()
        self.update()
