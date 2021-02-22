from app.product.action import (create, delete_register, filters, get_all,
                                get_by_id, update)
from app.product.schema import ProductSchema
from flask import Blueprint, jsonify, request

PRODUCT_SCHEMA = ProductSchema()
app_product = Blueprint('app_product', __name__)


@app_product.route('/product', methods=['POST'])
def create_product():
    data = request.json
    product = create(data)
    return PRODUCT_SCHEMA.dump(product), 201


@app_product.route('/product', methods=['GET'])
def get_all_product():
    if request.args.get('all'):
        return jsonify([PRODUCT_SCHEMA.dump(product) for product in get_all()]), 200
    payload = request.args.to_dict()
    products_found = filters(payload)
    # if products_found:
    return jsonify([PRODUCT_SCHEMA.dump(product) for product in products_found]), 200
    # return jsonify("No products found!"), 200


@app_product.route('/product/<id>', methods=['GET'])
def get_by_product_id(id: int):
    product = get_by_id(id)
    return PRODUCT_SCHEMA.dump(product), 200


@app_product.route('/product/<id>', methods=['PUT'])
def put_product(id: int):
    data = request.json
    product = update(data, id)
    return PRODUCT_SCHEMA.dump(product), 201


@app_product.route('/product/<id>', methods=['DELETE'])
def delete_product(id: int):
    product = delete_register(id)
    return jsonify(""), 204
