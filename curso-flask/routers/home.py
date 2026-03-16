from flask import render_template, request, Blueprint, jsonify
from models import Note
from services.time import now_utc

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    message = request.args.get("message")
    error = request.args.get("error")
    role = "user"
    notes = Note.query.all()
    now = now_utc()
    return render_template(
        "home.html", notes=notes, now=now, message=message, error=error
    )


@home_bp.route("/about")
def about():
    return "This home_bp is the note"


@home_bp.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return "Form send correctly", 201
    return "Page to contact"


@home_bp.route("/api/info")
def api_info():
    data = {"name": "Note home_bp", "version": "1.1.1"}
    return jsonify(data), 200


@home_bp.route("/confirmation", methods=["GET", "POST"])
def confirmation():
    print(request)
    value: str = request.args.get("note", "Not found")
    data = {"status": "OK", "value": value}
    return jsonify(data), 200