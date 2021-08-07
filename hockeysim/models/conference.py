from hockeysim.database import db, Model, Column
from sqlalchemy.sql import func
from .base import BaseModel


class Conference(BaseModel, Model):
    __tablename__ = 'conferences'

    def __init__(self, name, abreviation = None) -> None:
        self.name = name
        if abreviation is not None:
            self.abreviation = abreviation
        else:
            self.abreviation = self.name.upper()

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(255))
    abreviation = Column(db.String(3))
    divisions = db.relationship("Division", back_populates="conference")
    created_at = BaseModel.timestampColumn()
    updated_at = BaseModel.timestampColumn(True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "abreviation": self.abreviation,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def __repr__(self) -> str:
        return self._repr(
            id=self.id,
            name=self.name,
            abreviation=self.abreviation,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
