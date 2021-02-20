
from app.salesman.action import create, delete_register, get_all, get_by_id, update
from flask import Blueprint, jsonify, request

app_salesman = Blueprint('app_salesman', __name__)


@app_salesman.route('/salesman', methods=['POST'])
def create_salesman():
    data = request.json
    salesman = create(data)
    return jsonify(salesman.serialize()), 201


@app_salesman.route('/salesman', methods=['GET'])
def get_all_salesman():
    return jsonify([salesman.serialize() for salesman in get_all()]), 200


@app_salesman.route('/salesman/<id>', methods=['GET'])
def get_by_salesman_id(id: int):
    salesman = get_by_id(id)
    return jsonify(salesman.serialize()), 200


@app_salesman.route('/salesman/<id>', methods=['PUT'])
def put_salesman(id: int):
    data = request.json
    salesman = update(data, id)
    return jsonify(salesman.serialize()), 201


@app_salesman.route('/salesman/<id>', methods=['DELETE'])
def delete_salesman(id: int):
    salesman = delete_register(id)
    return jsonify(""), 204
