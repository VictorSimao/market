from app.salesman.model import Salesman
from database.repository import commit, delete, save


def get_all():
    return Salesman.query.all()


def get_by_id(id: str):
    return Salesman.query.get(id)


def create(data: dict):
    return save(Salesman(
        fantasy_name=data['fantasy_name'],
        company_name=data['company_name'],
        cnpj=data['cnpj'],
        email=data['email'],
        phone=data['phone'],
        address=data['address']
    ))


def update(data: dict, id: str):
    Salesman(fantasy_name=data['fantasy_name'], company_name=data['company_name'],
             cnpj=data['cnpj'], email=data['email'], phone=data['phone'], address=data['address'])
    Salesman.query.filter_by(id=id).update(dict(
        fantasy_name=f'{data["fantasy_name"]}', company_name=f'{data["company_name"]}',
        cnpj=f'{data["cnpj"]}', phone=f'{data["phone"]}', address=f'{data["address"]}'))
    commit()
    return get_by_id(id)


def delete_register(id: int):
    salesman = get_by_id(id)
    return delete(salesman)
