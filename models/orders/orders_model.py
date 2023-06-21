from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from peewee import fn
from orm import Order, OrderToProduct, OrderStatus
import decimal
from utils import normalise_number


class OrdersModel(QtCore.QAbstractTableModel):
    cols = [
        'Заказчик',
        'Дата доставки',
        'Адресс доставки',
        'Статус заказа'
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.orders = []
        self.update()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            order = self.orders[index.row()]

            return [
                order.client.company,
                str(order.delivery_date),
                order.adress,
                order.status.name

            ][index.column()]

    def update(self):
        self.orders = Order.select()
        self.layoutChanged.emit()

    def rowCount(self, index):
        return len(self.orders)

    def columnCount(self, index):
        return len(self.cols)

    def headerData(self, column, orientation, role=QtCore.Qt.DisplayRole):
        if not role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if orientation == QtCore.Qt.Horizontal:
            return QtCore.QVariant(self.cols[column])

    def create_order(self,
                     client,
                     delivery_date,
                     adress,
                     status,
                     products
                     ):
        order = Order.create(
            client=client,
            delivery_date=delivery_date,
            adress=adress,
            status=status,
        )
        for order_product in products:
            OrderToProduct.get_or_create(order=order, product=order_product[0], amount=order_product[1])
        self.update()

    def update_order(self,
                     index,
                     client,
                     delivery_date,
                     adress,
                     status,
                     products):

        order = self.orders[index.row()]

        order.client = client
        order.delivery_date = delivery_date
        order.adress = adress
        order.status = status

        order.save()

        OrderToProduct.delete().where(OrderToProduct.order == order).execute()

        for product in products:
            OrderToProduct.create(
                product=product[0],
                order=order,
                amount=product[1]
            )

        self.update()

    def delete_order(self, index):
        self.orders[index.row()].delete_instance(recursive=True)
        self.update()
