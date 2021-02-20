from uuid import uuid4
from re import match

from app.exceptions import ConflictException
from database import db
from sqlalchemy.orm import validates


class Marketplace(db.Model):
    __tablename__ = "marketplace"
    id = db.Column(db.String(36), default=lambda: str(
        uuid4()), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(240), nullable=False)
    site = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    technical_contact = db.Column(db.String(80), nullable=False)

    @validates('name')
    def name_validate(self, key, name: str):
        if not name:
            raise ConflictException(msg='Marketplace name is empty')
        return name

    @validates('description')
    def description_validate(self, key, description: str):
        if not description:
            raise ConflictException(msg='Marketplace description is empty')
        return description

    @validates('site')
    def site_validate(self, key, site: str):
        if not site:
            raise ConflictException(msg='Marketplace site is empty')
        return site

    @validates('phone')
    def phone_validate(self, key, phone: str):
        if not phone:
            raise ConflictException(msg="Marketplace phone number is empty")
        if len(phone) < 9:
            raise ConflictException(msg='Marketplace phone number invalid')
        if not phone.isdigit():
            raise ConflictException(msg='Use only numbers in marketplace phone')
        return phone

    @validates('email')
    def email_validate(self, key, email: str):
        if not email:
            raise ConflictException(msg="Marketplace email is empty")
        if not match(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', email):
            raise ConflictException(msg="Marketplace email is invalid")
        return email

    @validates('technical_contact')
    def technical_contact_validate(self, key, technical_contact: str):
        if not technical_contact:
            raise ConflictException(msg='Marketplace technical contact is empty')
        return technical_contact

    def serialize(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "site": self.site,
            "email": self.email,
            "phone": self.phone,
            "technical_contact": self.technical_contact
        }
