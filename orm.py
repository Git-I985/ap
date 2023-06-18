from peewee import *
from playhouse.migrate import *

# db = SqliteDatabase('app.db')
db = MySQLDatabase('alinaproj', user='root', password='root',
                   host='localhost', port=3306)


class BaseModel(Model):
    class Meta:
        database = db


class Units(BaseModel):
    name = TextField()


class Client(BaseModel):
    company = TextField()
    adress = TextField()
    phone = TextField()
    mail = TextField()


class OrderStatus(BaseModel):
    name = TextField()


class Order(BaseModel):
    client = ForeignKeyField(Client, backref='orders')
    delivery_date = DateTimeField()
    adress = TextField()
    status = ForeignKeyField(OrderStatus)


class Supplier(BaseModel):
    company = TextField()
    adress = TextField()
    phone = TextField()
    mail = TextField()


class DeliveryStatus(BaseModel):
    name = TextField()


class Delivery(BaseModel):
    supplier = ForeignKeyField(Supplier, backref='deliveries')
    date = DateTimeField()
    status = ForeignKeyField(DeliveryStatus)


class ProductCategory(BaseModel):
    name = TextField()


class Product(BaseModel):
    name = TextField()
    category = ForeignKeyField(ProductCategory)
    sale_price = DecimalField(null=True)
    buy_price = DecimalField()
    unit = ForeignKeyField(Units)
    margin = DecimalField()


class DeliveryToProduct(BaseModel):
    delivery = ForeignKeyField(Delivery)
    product = ForeignKeyField(Product)
    amount = DecimalField()


class OrderToProduct(BaseModel):
    order = ForeignKeyField(Order)
    product = ForeignKeyField(Product)
    amount = DecimalField()


class Warehouse(BaseModel):
    product = ForeignKeyField(Product, backref='in_stock')
    amount = DecimalField()


class UserRole(BaseModel):
    name = TextField()


class User(BaseModel):
    name = TextField()
    login = TextField()
    password = TextField()
    role = ForeignKeyField(UserRole)


def create_tables():
    with db:
        db.create_tables([
            Order,
            Client,
            Supplier,
            Delivery,
            DeliveryStatus,
            DeliveryToProduct,
            OrderStatus,
            OrderToProduct,
            Product,
            ProductCategory,
            Warehouse,
            Units,
            User,
            UserRole
        ])


create_tables()

# https://docs.peewee-orm.com/en/latest/peewee/playhouse.html?highlight=ALTER%20TABLE#example-usage
# migrator = SqliteMigrator(db)
# migrate(
#     # migrator.add_column('product', 'sale_price', DecimalField(null=True)),
#     # migrator.add_column('product', 'buy_price', DecimalField(null=True)),
#     migrator.add_column('product', 'unit_id', IntegerField(null=True)),
#     migrator.add_foreign_key_constraint('product', 'unit_id', ForeignKeyField(Units)),
#     # migrator.add_column('product', 'margin', DecimalField(null=True)),
# )
