from flask import Flask, redirect, request, jsonify, render_template, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from config import setting

app = Flask(__name__)

url_connection = setting.DATABASE_URL

app.config["SQLALCHEMY_DATABASE_URI"] = url_connection
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Nore(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True)
    content = db.Column(db.String(200), nullable=True)
    
    def __repr__(self):
        return f"<Note {self.id}: {self.title}"
    
@app.route("/")
def hello():
    role = "user"
    notes = [
        {
            "title": "Note 1",
            "created_at": datetime.now().strftime("%Y-%m-%d"),
            "completed": True,
        },
        {
            "title": "Note 2",
            "created_at": datetime.now().strftime("%Y-%m-%d"),
            "completed": False,
        },
        {
            "title": "Note 3",
            "created_at": datetime.now().strftime("%Y-%m-%d"),
            "completed": True,
        },
    ]
    return render_template("home.html", role=role, notes=notes)


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
    data = {"nombre": "Note app", "version": "1.1.1"}
    return jsonify(data), 200

@app.route("/confirmation", methods=["GET", "POST"])
def confirmation():    
    print(request)    
    value:str = request.args.get("note", "Not found")
    data = {"status":"OK", "value": value}    
    return jsonify(data), 200

@app.route("/create-note", methods=["GET", "POST"])
def create_note():
    if request.method == "POST":
        note = request.form.get(
            "note", "Not found"
        )  # The note was definid it in "note_from.html" file
        return redirect(
            url_for("confirmation", note=note)
        )
    return render_template("note_from.html")
