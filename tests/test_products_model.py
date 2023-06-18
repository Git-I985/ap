import unittest
from models import ProductsModel
from orm import Product, Warehouse, Units, ProductCategory
from peewee import SqliteDatabase

test_db = SqliteDatabase(':memory:')

models = [
    Product,
    Warehouse, Units, ProductCategory
]


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        for model in models:
            model.bind(test_db, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(models)
        Units.create(name='Test unit')
        ProductCategory.create(name='Test category')
    
    def test_create_product(self):
        products_model = ProductsModel(product_model=Product, warehouse_model=Warehouse)
        products_model.create_product(
            name='Test product name',
            category=ProductCategory.select()[0],
            sale_price='12',
            buy_price='12',
            unit=Units.select()[0],
            margin='12',
        )
        created_product = products_model.products[0]
        self.assertEqual(1, len(products_model.products))
        self.assertEqual('Test product name', created_product.name)
        self.assertEqual('Test category', created_product.category.name)
        self.assertEqual('Test unit', created_product.unit.name)

    # def delete_product(self):
    #     raise NotImplementedError
    #
    # def update_product(self):
    #     raise NotImplementedError
    #
    # def test(self):
    #     print(products_model.products)

    def tearDown(self):
        test_db.drop_tables(models)
        test_db.close()
