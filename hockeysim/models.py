from flask import current_app
from hockeysim import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def serialize(self):
        return {"id": self.id,
                "username": self.username,
                "email": self.email}

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Post %r>' % self.title