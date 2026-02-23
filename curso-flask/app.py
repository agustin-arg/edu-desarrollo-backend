from flask import Flask, redirect, request, jsonify, render_template, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from config import setting

app = Flask(__name__)

url_connection = setting.DATABASE_URL

app.config["SQLALCHEMY_DATABASE_URI"] = url_connection
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True)
    content = db.Column(db.String(200), nullable=True)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.strftime(datetime.today(), "%b %d %Y"),
    )

    def __repr__(self):
        return f"<Note {self.id}: {self.title}"


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    role = "user"
    notes = Note.query.all()
    return render_template("home.html", notes=notes)


@app.route("/about")
def about():
    return "This app is the note"


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return "Form send correctly", 201
    return "Page to contact"


@app.route("/api/info")
def api_info():
    data = {"name": "Note app", "version": "1.1.1"}
    return jsonify(data), 200


@app.route("/confirmation", methods=["GET", "POST"])
def confirmation():
    print(request)
    value: str = request.args.get("note", "Not found")
    data = {"status": "OK", "value": value}
    return jsonify(data), 200


@app.route("/create-note", methods=["GET", "POST"])
def create_note():
    if request.method == "POST":
        title = request.form.get("title", "")
        content = request.form.get("content", "")
        db_note = Note(title=title, content=content)
        db.session.add(db_note)
        db.session.commit()
        return redirect(url_for("home", note=db_note))
    return render_template("note_from.html")