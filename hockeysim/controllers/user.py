from flask import Blueprint, render_template, session, abort, request, jsonify
from hockeysim.database import db
from hockeysim.models.user import User

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    email = data['email']

    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize())
