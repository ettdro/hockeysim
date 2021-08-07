from hockeysim.database import db
from sqlalchemy.sql import func


class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(255))
    name = db.Column(db.String(255))
    abreviation = db.Column(db.String(3))
    division_id = db.Column(db.Integer, db.ForeignKey('divisions.id'))
    division = db.relationship("Division", back_populates="teams")
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=func.now(), onupdate=func.now())

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "abreviation": self.abreviation,
            "division": self.division,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __repr__(self):
        return '<Team %r>' % self.division
