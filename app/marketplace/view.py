from app.marketplace.action import (create, delete_register, get_all,
                                    get_by_id, update)
from flask import Blueprint, jsonify, request

app_marketplace = Blueprint('app_marketplace', __name__)


@app_marketplace.route('/marketplace', methods=['POST'])
def create_marketplace():
    data = request.json
    marketplace = create(data)
    return jsonify(marketplace.serialize()), 201


@app_marketplace.route('/marketplace', methods=['GET'])
def get_all_marketplace():
    return jsonify([marketplace.serialize() for marketplace in get_all()]), 200


@app_marketplace.route('/marketplace/<id>', methods=['GET'])
def get_by_marketplace_id(id: int):
    marketplace = get_by_id(id)
    return jsonify(marketplace.serialize()), 200


@app_marketplace.route('/marketplace/<id>', methods=['PUT'])
def put_marketplace(id: int):
    data = request.json
    marketplace = update(data, id)
    return jsonify(marketplace.serialize()), 201


@app_marketplace.route('/marketplace/<id>', methods=['DELETE'])
def delete_marketplace(id: int):
    marketplace = delete_register(id)
    return jsonify(""), 204
