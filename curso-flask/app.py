from flask import Flask, redirect, request, jsonify, render_template, url_for
from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy
from config import setting

app = Flask(__name__)

url_connection = setting.DATABASE_URL

app.config["SQLALCHEMY_DATABASE_URI"] = url_connection
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# --- Date utilities ---
def now_utc():
    """Return timezone-aware current UTC datetime."""
    return datetime.now()


def parse_datetime(value: str):
    """Try parsing a date/time string into a timezone-aware datetime (UTC).

    Supports several common formats. Returns None if parsing fails or
    if `value` is falsy.
    """
    if not value:
        return None
    formats = ("%Y-%m-%d", "%Y-%m-%d %H:%M", "%d/%m/%y", "%d/%m/%y %H:%M")
    for fmt in formats:
        try:
            dt = datetime.strptime(value, fmt)
            return dt.replace(tzinfo=timezone.utc)
        except Exception:
            continue
    return None


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, nullable=True, default=now_utc)
    edited_at = db.Column(db.DateTime, nullable=True)
    post_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<Note {self.id}: {self.title}"


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    role = "user"
    notes = Note.query.all()
    now = now_utc()
    return render_template("home.html", notes=notes, now=now)


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
        post = request.form.get("post", "")
        # parse `post` into timezone-aware datetime objects
        post_dt = parse_datetime(post)
        db_note = Note(title=title, content=content, post_at=post_dt)
        db.session.add(db_note)
        db.session.commit()
        return redirect(url_for("home"))
    now = now_utc()
    return render_template("note_from.html", now=now)


@app.route("/edit-note/<int:id>", methods=["GET", "POST"])
def edit_note(id):
    note = Note.query.get_or_404(id)
    if request.method == "POST":
        title = request.form.get("title", "")
        content = request.form.get("content", "")
        content = request.form.get("content", "")
        post = request.form.get("post", "")
        note.title = title
        note.content = content
        note.post_at = parse_datetime(post)
        note.edited_at = now_utc()
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_note.html", note=note)


@app.route("/delete-note/<int:id>", methods=["POST"])
def delete_note(id):
    note = Note.query.get(id)
    if not note:
        return redirect(url_for("home"))
    db.session.delete(note)
    db.session.commit()

    return redirect(url_for("home"))
