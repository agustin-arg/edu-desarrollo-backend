from flask_sqlalchemy import SQLAlchemy
from config import setting

url_connection = setting.DATABASE_URL
secret_key = setting.SECRET_KEY

db = SQLAlchemy()


def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = url_connection
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = secret_key
    db.init_app(app)
