from models.clients_model import ClientsModel
from models.products_categories_model import ProductsCategoriesModel
from models.products_model import ProductsModel
from models.products_units_model import ProductsUnitsModel
from orm import Product, Warehouse

products_model = ProductsModel(product_model=Product, warehouse_model=Warehouse)
clients_model = ClientsModel()
units_model = ProductsUnitsModel()
product_categories_model = ProductsCategoriesModel()
