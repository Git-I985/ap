from PyQt5 import QtWidgets, QtGui
from models import suppliers_model
from uic.createupdatesupplier import Ui_CreateUpdateSupplier


class CreateUpdateSuppliersWindow(QtWidgets.QMainWindow, Ui_CreateUpdateSupplier):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_CreateUpdateSupplier, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_click)
        self.update_index = None

    def on_click(self):
        if self.update_index:
            self.update_supplier(self.update_index)
        else:
            self.create_supplier()

    def create_supplier(self):
        suppliers_model.create_supplier(
            company=self.lineEdit.text(),
            adress=self.lineEdit_2.text(),
            phone=self.lineEdit_3.text(),
            mail=self.lineEdit_4.text()
        )
        self.close()

    def update_supplier(self, index):
        suppliers_model.update_supplier(
            index,
            company=self.lineEdit.text(),
            adress=self.lineEdit_2.text(),
            phone=self.lineEdit_3.text(),
            mail=self.lineEdit_4.text()
        )
        self.close()
        self.update_index = None

    def load_supplier(self, index):
        self.update_index = index
        self.pushButton.setText('Изменить данные поставщика')
        self.setWindowTitle('Изменить данные поставщика')

        supplier = suppliers_model.suppliers[index.row()]

        self.lineEdit.setText(supplier.company)
        self.lineEdit_2.setText(supplier.adress)
        self.lineEdit_3.setText(supplier.phone)
        self.lineEdit_4.setText(supplier.mail)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.pushButton.setText('Сохранить')
        self.setWindowTitle('Добавить поставщика')
