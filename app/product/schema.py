from database import ma
from marshmallow import fields

from app.category.schema import CategorySchema
from app.product.model import Product


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product()
    
    categories = fields.List(fields.Nested(CategorySchema(only=('name',))))