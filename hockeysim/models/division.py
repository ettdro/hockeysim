from hockeysim.database import db
from sqlalchemy.sql import func


class Division(db.Model):
    __tablename__ = 'divisions'

    def __init__(self, name, abreviation) -> None:
        self.name = name
        self.abreviation = abreviation

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    abreviation = db.Column(db.String(3))
    conference_id = db.Column(db.Integer, db.ForeignKey('conferences.id'))
    conference = db.relationship("Conference", back_populates="divisions")
    teams = db.relationship("Team", back_populates="division")
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=func.now(), onupdate=func.now())

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "abreviation": self.abreviation,
            "conference": self.conference,
            "teams": self.teams,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __repr__(self):
        return '<Division %r>' % self.name
