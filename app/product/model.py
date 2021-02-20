from uuid import uuid4
import re

from app.exceptions import ConflictException
from database import db
from sqlalchemy.orm import validates


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.String(36), default=lambda: str(
        uuid4()), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(240), nullable=False)
    price = db.Column(db.Float(10), nullable=False)

    @validates('name')
    def name_validate(self, key, name: str):
        if not name:
            raise ConflictException(msg='Product name is empty')
        return name

    @validates('description')
    def description_validate(self, key, description: str):
        if not description:
            raise ConflictException(msg='Product description is empty')
        return description

    @validates('price')
    def price_validate(self, key, price: str):
        if not price:
            raise ConflictException(msg='Product price is empty')
        if re.findall('[a-zA-Z_+-,@#$%¨&*^~`´]', price):
            raise ConflictException(msg='Use only numbers and point in product price')
        return price
    
    def serialize(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price
        }

