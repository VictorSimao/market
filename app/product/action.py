from app.product.model import Product
from database.repository import commit, delete, save


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
