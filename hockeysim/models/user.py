from hockeysim.database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def serialize(self):
        return {"id": self.id,
                "username": self.username,
                "email": self.email}

    def __repr__(self):
        return '<User %r>' % self.username
