from flask import redirect, render_template, request, url_for, Blueprint, flash
from db import db
from models import Note
from services.time import parse_datetime, now_utc

note_bp = Blueprint("notes", __name__)


@note_bp.route("/create-note", methods=["GET", "POST"])
def create_note():
    if request.method == "POST":
        title = request.form.get("title", "")
        content = request.form.get("content", "")
        post = request.form.get("post", "")
        post_dt = parse_datetime(post)
        db_note = Note(title=title, content=content, post_at=post_dt)
        db.session.add(db_note)
        db.session.commit()
        flash(message="Note successfully created", category="success")
        return redirect(url_for("home.home"))
    now = now_utc()
    return render_template("create_note.html", now=now)


@note_bp.route("/edit-note/<int:id>", methods=["GET", "POST"])
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
        return redirect(url_for("home.home"))
    return render_template("edit_note.html", note=note)


@note_bp.route("/delete-note/<int:id>", methods=["post"])
def delete_note(id):
    note = Note.query.get(id)
    if not note:
        return redirect(url_for("home.home", error="Note not found"))
    db.session.delete(note)
    db.session.commit()
    flash(message="Note successfully deleted", category="success")
    return redirect(url_for("home.home", message="Note successfully deleted"))


@note_bp.route("/confirmation/<int:id>")
def confirmation_delete_note(id):
    return render_template("confirmation_delete_note.html", id=id)
