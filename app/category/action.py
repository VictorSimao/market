from app.category.model import Category
from app.product.action import get_by_id as get_product_by_id
from database.repository import commit, delete, save


def get_all():
    return Category.query.all()


def get_by_id(id: str):
    return Category.query.get(id)


def create(data: dict):
    return save(Category(
        name=data['name'],
        description=data['description']
    ))


def update(data: dict, id: str):
    Category(name=data['name'], description=data['description'])
    Category.query.filter_by(id=id).update(
        dict(name=f'{data["name"]}', description=f'{data["description"]}'))
    commit()
    return get_by_id(id)


def delete_register(id: int):
    category = get_by_id(id)
    return delete(category)


def update_category_with_product(category_id: str, product_id: str):
    category = get_by_id(category_id)
    product = get_product_by_id(product_id)
    category.product.append(product)
    save(category)
    category_serialize = category.serialize()
    category_serialize.update({'product_id': product_id, 'product_name': product.name})
    return category_serialize
