from models.clients.clients_model import ClientsModel
from models.products.products_categories_model import ProductsCategoriesModel
from models.products.products_model import ProductsModel
from models.products.products_units_model import ProductsUnitsModel
from models.users.users_model import UsersModel
from models.users.user_role_model import UsersRolesModel
from models.suppliers.suppliers_model import SuppliersModel
from models.warehouse.warehouse_model import WarehouseModel
from models.orders.orders_model import OrdersModel
from models.orders.order_status_model import OrderStatusModel
from models.deliveries.delivery_model import DeliveriesModel
from models.deliveries.delivery_status_model import DeliveryStatusModel
from orm import Product, Warehouse

# Инициализация глобальных моделей данных, инициализация моделей глобальна в целях использования
# каждой из них в нескольких представлениях (каждая модель может использоваться более чем в одном представлении
# поэтому инициализируется отдельно)
products_model = ProductsModel(product_model=Product, warehouse_model=Warehouse)
clients_model = ClientsModel()
suppliers_model = SuppliersModel()
units_model = ProductsUnitsModel()
product_categories_model = ProductsCategoriesModel()
users_model = UsersModel()
users_roles_model = UsersRolesModel()
warehouse_model = WarehouseModel()
orders_model = OrdersModel()
order_status_model = OrderStatusModel()

delivery_model = DeliveriesModel()
delivery_status_model = DeliveryStatusModel()
