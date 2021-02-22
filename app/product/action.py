import re

from app.product.model import Product
from app.product.schema import ProductSchema
from database.repository import commit, delete, save

PRODUCT_SCHEMA = ProductSchema()


def get_all():
    return Product.query.all()


def get_by_id(id: str):
    return Product.query.get(id)


def create(data: dict):
    return save(Product(
        name=data['name'],
        description=data['description'],
        price=data['price']
    ))


def update(data: dict, id: str):
    Product(name=data['name'], description=data['description'],
            price=data['price'])
    Product.query.filter_by(id=id).update(dict(
        name=f'{data["name"]}', description=f'{data["description"]}',
        price=f'{data["price"]}'))
    commit()
    return get_by_id(id)


def delete_register(id: int):
    product = get_by_id(id)
    return delete(product)


def filters(data: dict):
    products = []
    all_products = get_all()
    for product in all_products:
        products_valid = []
        if data.get('name'):
            if data['name'] == product.name:
                products_valid.append(True)
            else:
                products_valid.append(False)
        if data.get('price'):
            if data['price'] == str(product.price):
                products_valid.append(True)
            else:
                products_valid.append(False)
        if data.get('description'):
            if data['description'] == product.description:
                products_valid.append(True)
            else:
                products_valid.append(False)
        if data.get('category'):
            categories_valid = []
            for category in product.categories:
                if data['category'] == category.name:
                    categories_valid.append(True)
                else:
                    categories_valid.append(False)
            if any(categories_valid):
                products_valid.append(True)
            else:
                products_valid.append(False)
        if all(products_valid):
            products.append(product)
    return products
