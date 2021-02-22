from app.category.model import Category
from database.repository import commit, delete, save


def get_all():
    return Category.query.all()


def get_by_id(id: str):
    return Category.query.get(id)


def create(data: dict):
    return save(Category(
        name=data['name'],
        description=data['description'],
        product_id=data['product_id']
    ))


def update(data: dict, id: str):
    Category(name=data['name'], description=data['description'])
    Category.query.filter_by(id=id).update(
        dict(name=f'{data["name"]}', description=f'{data["description"]}', product_id=f'{data["product_id"]}'))
    commit()
    return get_by_id(id)


def delete_register(id: int):
    category = get_by_id(id)
    return delete(category)
