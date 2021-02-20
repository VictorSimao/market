from app.marketplace.model import Marketplace
from database.repository import commit, delete, save


def get_all():
    return Marketplace.query.all()


def get_by_id(id: str):
    return Marketplace.query.get(id)


def create(data: dict):
    return save(Marketplace(
        name=data['name'],
        description=data['description'],
        site=data['site'],
        email=data['email'],
        phone=data['phone'],
        technical_contact=data['technical_contact']
    ))


def update(data: dict, id: str):
    Marketplace(name=data['name'], description=data['description'],
                site=data['site'], email=data['email'], phone=data['phone'], 
                technical_contact=data['technical_contact'])
    Marketplace.query.filter_by(id=id).update(dict(
        name=f'{data["name"]}', description=f'{data["description"]}',
        site=f'{data["site"]}', phone=f'{data["phone"]}', 
        technical_contact=f'{data["technical_contact"]}'))
    commit()
    return get_by_id(id)


def delete_register(id: int):
    marketplace = get_by_id(id)
    return delete(marketplace)
