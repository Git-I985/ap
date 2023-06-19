from models.clients_model import ClientsModel
from models.products_categories_model import ProductsCategoriesModel
from models.products_model import ProductsModel
from models.products_units_model import ProductsUnitsModel
from models.users_model import UsersModel
from orm import Product, Warehouse

# Инициализация глобальных моделей данных, инициализация моделей глобальна в целях использования
# каждой из них в нескольких представлениях (каждая модель может использоваться более чем в одном представлении
# поэтому инициализируется отдельно)
products_model = ProductsModel(product_model=Product, warehouse_model=Warehouse)
clients_model = ClientsModel()
units_model = ProductsUnitsModel()
product_categories_model = ProductsCategoriesModel()
users_model = UsersModel()
