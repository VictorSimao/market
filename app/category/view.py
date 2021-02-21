from app.category.action import (create, delete_register, get_all,
                                 get_by_id, update, update_category_with_product)
from flask import Blueprint, jsonify, request
from app.category.schema import CategorySchema

CATEGORY_SCHEMA = CategorySchema()
app_category = Blueprint('app_category', __name__)


@app_category.route('/category', methods=['POST'])
def create_category():
    data = request.json
    category = create(data)
    return CATEGORY_SCHEMA.dump(category), 201


@app_category.route('/category', methods=['GET'])
def get_all_category():
    return jsonify([CATEGORY_SCHEMA.dump(category) for category in get_all()]), 200


@app_category.route('/category/<id>', methods=['GET'])
def get_by_category_id(id: int):
    category = get_by_id(id)
    return CATEGORY_SCHEMA.dump(category), 200


@app_category.route('/category/<id>', methods=['PUT'])
def put_category(id: int):
    data = request.json
    category = update(data, id)
    return CATEGORY_SCHEMA.dump(category), 201


@app_category.route('/category/<id>', methods=['DELETE'])
def delete_category(id: int):
    category = delete_register(id)
    return jsonify(""), 204


@app_category.route('/category/<category_id>/product/<product_id>', methods=['POST'])
def update_relationship(category_id, product_id):
    table_updated = update_category_with_product(category_id, product_id)
    return jsonify(table_updated), 200
