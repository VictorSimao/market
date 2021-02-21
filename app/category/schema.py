from database import ma

from app.category.model import Category


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category()
    include_fk = True