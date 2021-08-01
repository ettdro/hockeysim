from .config import DevConfig, TestConfig
from flask import Flask, jsonify, request
from hockeysim.models import User

def create_app(testing=False):
    app = Flask(__name__)
    if testing:
        app.config.from_object(TestConfig)
    else:
        app.config.from_object(DevConfig)

    from hockeysim.models import db

    db.init_app(app)
    with app.app_context():
        db.create_all()

    @app.route('/register', methods=['POST'])
    def register():
        data = request.json
        username = data['username']
        email = data['email']
        
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return jsonify(user.serialize())
    
    return app