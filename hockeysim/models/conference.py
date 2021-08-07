from hockeysim.database import db, Model, Column
from sqlalchemy.sql import func


class Conference(Model):
    __tablename__ = 'conferences'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(255))
    abreviation = Column(db.String(3))
    divisions = db.relationship("Division", back_populates="conference")
    created_at = Column(db.DateTime, nullable=False, default=func.now())
    updated_at = Column(db.DateTime, nullable=False,
                        default=func.now(), onupdate=func.now())

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __repr__(self):
        return '<Post %r>' % self.title
