from PyQt5 import QtWidgets
from models import clients_model
from view.Clients.CreateUpdateClientWindow import CreateUpdateClientWindow
from uic.clients import Ui_Clients


# Класс ClientsWindow является окном и наследуется от QMainWindow и является основой для
# построения пользовательского интерфейса окна работы с клиентами в системе.
# Класс ClientsWindow содержит в себе инициализацию обработчиков событий исходящих от элементов
# внутри этого окна, а так-же устанавливает модели для элементов представлений и инициализирует интерфейс
# с использованием скомпилированных в py - ui файлов. Класс ClientsWindow так-же взаимодействует с моделями
# данных внутри обработчиков событий, вызывая методы моделей и меняя данные исходя из поведения пользователя.
class ClientsWindow(QtWidgets.QMainWindow, Ui_Clients):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_Clients, self).__init__()
        self.setupUi(self)

        self.createUpdateClientWindow = CreateUpdateClientWindow()
        self.pushButton.clicked.connect(lambda x: self.createUpdateClientWindow.show())
        self.pushButton_2.clicked.connect(self.delete_client)
        self.pushButton_3.clicked.connect(self.update_client)
        self.tableView.setModel(clients_model)
        self.tableView.resizeColumnsToContents()

    def delete_client(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        clients_model.delete_client(indexes[0])

    def update_client(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        self.createUpdateClientWindow.show()
        self.createUpdateClientWindow.load_client(indexes[0])
