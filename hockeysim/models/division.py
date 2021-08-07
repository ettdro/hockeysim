from hockeysim.database import Model, db
from sqlalchemy.sql import func
from .base import BaseModel


class Division(BaseModel, Model):
    __tablename__ = 'divisions'

    def __init__(self, name, abreviation = None) -> None:
        self.name = name
        if abreviation is not None:
            self.abreviation = abreviation
        else:
            self.abreviation = (self.name[0:3]).upper()

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    abreviation = db.Column(db.String(3))
    conference_id = db.Column(db.Integer, db.ForeignKey('conferences.id'))
    conference = db.relationship("Conference", back_populates="divisions")
    teams = db.relationship("Team", back_populates="division")
    created_at = BaseModel.timestampColumn()
    updated_at = BaseModel.timestampColumn(True)

    def serialize(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "abreviation": self.abreviation,
            "teams": self.teams,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __repr__(self) -> str:
        return self._repr(
            id=self.id,
            name=self.name,
            conference=self.conference,
            abreviation=self.abreviation,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
