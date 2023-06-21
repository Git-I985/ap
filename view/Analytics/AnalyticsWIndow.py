from PyQt5 import QtWidgets
from models import clients_model
from uic.analytics import Ui_MainWindow
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from orm import db

matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(2, 2, 1)
        self.axes2 = fig.add_subplot(2, 2, 2)
        self.axes3 = fig.add_subplot(2, 2, 3)
        self.axes4 = fig.add_subplot(2, 2, 4)
        super().__init__(fig)


class AnalyticsWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.setCentralWidget(self.sc)
        self.upd()

    def draw1(self):
        cursor = db.execute_sql(
            "SELECT product.name, COUNT(ordertoproduct.product_id) as 'count' FROM `ordertoproduct` INNER JOIN product ON product.id = ordertoproduct.product_id GROUP BY `product_id` ORDER BY count ASC")
        products_data = [row for row in cursor.fetchall()]
        products = [row[0] for row in products_data]
        sales = [row[1] for row in products_data]
        self.sc.axes.bar(products, sales)
        self.sc.axes.set_title('Рейтинг продаж продуктов по кол-ву')

    def draw2(self):
        cursor = db.execute_sql(
            "SELECT c.company, COUNT(client_id) as count FROM `order` INNER JOIN client c on `order`.client_id = c.id GROUP BY client_id ORDER BY count ASC")

        clients_data = [row for row in cursor.fetchall()]
        companies = [row[0] for row in clients_data]
        orders = [row[1] for row in clients_data]
        self.sc.axes2.bar(companies, orders)
        self.sc.axes2.set_title('Рейтинг заказчиков по кол-ву заказов')

    def draw3(self):
        cursor = db.execute_sql(
            "SELECT client.company, SUM(amount) as total_count, SUM(product.sale_price) as total_price FROM ordertoproduct INNER JOIN `order` ON ordertoproduct.order_id = `order`.id INNER JOIN `client` ON client.id = `order`.client_id INNER JOIN product ON product.id = `ordertoproduct`.product_id GROUP BY order_id ORDER BY total_count ASC;")
        cd = [row for row in cursor.fetchall()]
        companies = [row[0] for row in cd]
        total_counts = [row[1] for row in cd]
        self.sc.axes3.bar(companies, total_counts)
        self.sc.axes3.set_title('Рейтинг заказчиков по кол-ву заказанных товаров')

    def draw4(self):
        cursor = db.execute_sql(
            "SELECT client.company, SUM(amount) as total_count, SUM(product.sale_price) as total_price FROM ordertoproduct INNER JOIN `order` ON ordertoproduct.order_id = `order`.id INNER JOIN `client` ON client.id = `order`.client_id INNER JOIN product ON product.id = `ordertoproduct`.product_id GROUP BY order_id ORDER BY total_count ASC;")
        cd = [row for row in cursor.fetchall()]
        companies = [row[0] for row in cd]
        total_prices = [row[2] for row in cd]
        self.sc.axes4.bar(companies, total_prices)
        self.sc.axes4.set_title('Рейтинг заказчиков по сумме заказов товаров')

    def upd(self):
        self.draw1()
        self.draw2()
        self.draw3()
        self.draw4()
