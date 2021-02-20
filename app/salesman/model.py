from uuid import uuid4
from re import match

from app.salesman.exception import InvalidSalesmanException
from database import db
from sqlalchemy.orm import validates


class Salesman(db.Model):
    __tablename__ = 'salesman'
    id = db.Column(db.String(36), default=lambda: str(
        uuid4()), primary_key=True)
    fantasy_name = db.Column(db.String(80), nullable=False)
    company_name = db.Column(db.String(80), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(36), nullable=False)
    address = db.Column(db.String(240), nullable=False)

    @validates('fantasy_name')
    def fantasy_name_validate(self, key, fantasy_name: str):
        if not fantasy_name:
            raise InvalidSalesmanException(msg="Fantasy name is empty")
        return fantasy_name

    @validates('company_name')
    def company_name_validate(self, key, company_name: str):
        if not company_name:
            raise InvalidSalesmanException(msg="Company name is empty")
        return company_name

    @validates('cnpj')
    def cnpj_validate(self, key, cnpj: str):
        if not cnpj:
            raise InvalidSalesmanException(msg="CNPJ is empty")
        if len(cnpj) != 14:
            raise InvalidSalesmanException(msg='Invalid CNPJ')
        return cnpj

    @validates('email')
    def email_validate(self, key, email: str):
        if not email:
            raise InvalidSalesmanException(msg="Email is empty")
        if not match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email):
            raise InvalidSalesmanException(msg="Email is invalid")
        return email

    @validates('phone')
    def phone_validate(self, key, phone: str):
        if not phone:
            raise InvalidSalesmanException(msg="Phone number is empty")
        if len(phone) < 9:
            raise InvalidSalesmanException(msg='Phone number invalid')
        if not phone.isdigit():
            raise InvalidSalesmanException(msg='Use only numbers in Phone')
        return phone

    @validates('address')
    def address_validate(self, key, address: str):
        if not address:
            raise InvalidSalesmanException(msg="Address is empty")
        return address

    def serialize(self) -> dict:
        return {
            "id": self.id,
            "fantasy_name": self.fantasy_name,
            "company_name": self.company_name,
            "cnpj": self.cnpj,
            "email": self.email,
            "phone": self.phone,
            "address": self.address
        }
