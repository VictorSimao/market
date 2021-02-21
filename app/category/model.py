import re
from uuid import uuid4

from app.exceptions import ConflictException
from database import db
from sqlalchemy.orm import validates


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.String(36), default=lambda: str(
        uuid4()), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(240), nullable=False)
    product_id = db.Column(db.String(36), db.ForeignKey("product.id"))
    product = db.relationship("Product", back_populates="categories")

    @validates('name')
    def name_validate(self, key, name: str):
        if not name:
            raise ConflictException(msg='Category name is empty')
        return name

    @validates('description')
    def description_validate(self, key, description: str):
        if not description:
            raise ConflictException(msg='Category description is empty')
        return description
