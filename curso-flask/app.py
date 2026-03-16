from flask import Flask
from db import db, init_db
from routers.notes import note_bp
from routers.home import home_bp

app = Flask(__name__)
init_db(app)
app.register_blueprint(note_bp)
app.register_blueprint(home_bp)


with app.app_context():
    db.create_all()



