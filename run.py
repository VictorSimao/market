from flask import Blueprint, render_template

from database import db


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
