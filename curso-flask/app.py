from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)


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

@app.route("/create-note", methods=["GET", "POST"])
def create_note():
    return render_template("note_from.html")