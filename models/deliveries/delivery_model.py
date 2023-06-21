from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from peewee import fn
from orm import Delivery, Product, DeliveryToProduct
import decimal
from utils import normalise_number


class DeliveriesModel(QtCore.QAbstractTableModel):
    cols = [
        'Поставщик',
        'Дата доставки',
        'Статус поставки'
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.deliveries = []
        self.update()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            delivery = self.deliveries[index.row()]

            return [
                delivery.supplier.company,
                str(delivery.date),
                delivery.status.name
            ][index.column()]

    def update(self):
        self.deliveries = Delivery.select()
        self.layoutChanged.emit()

    def rowCount(self, index):
        return len(self.deliveries)

    def columnCount(self, index):
        return len(self.cols)

    def headerData(self, column, orientation, role=QtCore.Qt.DisplayRole):
        if not role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if orientation == QtCore.Qt.Horizontal:
            return QtCore.QVariant(self.cols[column])

    def create_delivery(self,
                        supplier,
                        date,
                        status,
                        products
                        ):
        pass
        delivery = Delivery.create(
            supplier=supplier,
            date=date,
            status=status,
        )
        for delivery_product in products:
            DeliveryToProduct.get_or_create(
                delivery=delivery,
                product=delivery_product[0],
                amount=delivery_product[1])
        self.update()

    def update_delivery(self,
                        index,
                        supplier,
                        date,
                        status,
                        products):

        delivery = self.deliveries[index.row()]

        delivery.supplier = supplier
        delivery.date = date
        delivery.status = status

        delivery.save()

        DeliveryToProduct.delete().where(DeliveryToProduct.delivery == delivery).execute()

        for product in products:
            DeliveryToProduct.create(
                product=product[0],
                delivery=delivery,
                amount=product[1]
            )

        self.update()

    def delete_delivery(self, index):
        self.deliveries[index.row()].delete_instance(recursive=True)
        self.update()
