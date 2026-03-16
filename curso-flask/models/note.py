from db import db
from services.time import now_utc

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, nullable=True, default=now_utc)
    edited_at = db.Column(db.DateTime, nullable=True)
    post_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<Note {self.id}: {self.title}"