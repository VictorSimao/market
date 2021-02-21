from database import db, migrate
from flask import Flask
from flask_cors import CORS

from app.category.view import app_category
from app.marketplace.view import app_marketplace
from app.product.view import app_product
from app.salesman.view import app_salesman


def create_app():
    app = Flask(__name__)
    CORS(app, resource={r"*": {"origins": "*"}})
    _register_blueprint(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
    _register_blueprint(app)
    return app


def _register_blueprint(app):
    app.register_blueprint(app_salesman)
    app.register_blueprint(app_marketplace)
    app.register_blueprint(app_product)
    app.register_blueprint(app_category)
