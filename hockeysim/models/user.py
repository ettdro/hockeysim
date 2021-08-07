from hockeysim.database import Model, db
from .base import BaseModel


class User(BaseModel, Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    created_at = BaseModel.timestampColumn()
    updated_at = BaseModel.timestampColumn(True)

    def serialize(self):
        return {"id": self.id,
                "username": self.username,
                "email": self.email}

    def __repr__(self) -> str:
        return self._repr(
            id=self.id,
            username=self.username,
            email=self.email,
            created_at=self.created_at,
            updated_at=self.updated_at
        )