from hockeysim.models.base import BaseModel
from hockeysim.models.conference import Conference
from hockeysim.database import Model, db
from .base import BaseModel


class Team(BaseModel, Model):
    __tablename__ = 'teams'

    def __init__(self, city, name, abreviation = None) -> None:
        self.city = city
        self.name = name
        if abreviation is not None:
            self.abreviation = abreviation
        else:
            self.abreviation = (self.city[0:3]).upper()

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(255))
    name = db.Column(db.String(255))
    abreviation = db.Column(db.String(3))
    division_id = db.Column(db.Integer, db.ForeignKey('divisions.id'))
    division = db.relationship("Division", back_populates="teams")
    created_at = BaseModel.timestampColumn()
    updated_at = BaseModel.timestampColumn(True)

    def serialize(self) -> dict:
        return {
            "id": self.id,
            "city": self.city,
            "name": self.name,
            "abreviation": self.abreviation,
            "division": self.division,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __repr__(self) -> str:
        return self._repr(
            id=self.id,
            city=self.city,
            name=self.name,
            abreviation=self.abreviation,
            division=self.division,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
