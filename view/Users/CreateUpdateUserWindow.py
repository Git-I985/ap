from PyQt5 import QtWidgets, QtGui
from models import users_roles_model, users_model
from uic.createupdateuser import Ui_MainWindow
from utils import hash_password


class CreateUpdateUserWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_click)
        self.comboBox.setModel(users_roles_model)
        self.update_index = None
        self.label_2.hide()
        self.lineEdit_2.hide()

    def on_click(self):
        if self.update_index:
            self.update_user(self.update_index)
        else:
            self.create_user()

    def create_user(self):
        users_model.create_user(
            login=self.lineEdit.text(),
            password=hash_password(self.lineEdit_3.text()),
            role=users_roles_model.users_roles[self.comboBox.currentIndex()],
        )
        self.close()

    def update_user(self, index):
        print('update')
        old_password = hash_password(self.lineEdit_3.text())
        new_password = hash_password(self.lineEdit_2.text())
        user = users_model.users[index.row()]

        if not old_password == user.password and len(new_password):
            QtWidgets.QMessageBox.critical(
                self,
                "Ошибка",
                "Не верный старый пароль"
            )
            return

        users_model.update_user(
            index,
            login=self.lineEdit.text(),
            password=new_password,
            role=users_roles_model.users_roles[self.comboBox.currentIndex()],
        )

        self.close()
        self.update_index = None

    def load_user(self, index):
        self.update_index = index
        self.pushButton.setText('Изменить данные пользователя')
        self.setWindowTitle('Изменить данные пользователя')

        user = users_model.users[index.row()]

        self.lineEdit.setText(user.login)
        self.lineEdit_2.show()
        self.comboBox.setCurrentIndex(list(users_roles_model.users_roles).index(user.role))
        self.label_2.show()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.comboBox.setCurrentIndex(0)
        self.pushButton.setText('Сохранить')
        self.setWindowTitle('Добавить пользователя')
