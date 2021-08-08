from flask import Blueprint, request
from hockeysim.database import db
from hockeysim.models.conference import Conference

conference_routes = Blueprint('conference_routes', __name__)

@conference_routes.route('/conferences/create', methods=['POST'])
def create():
    data = request.json
    name = data['name']
    abreviation = data['abreviation'] if 'abreviation' in data else None

    conference = Conference(name=name, abreviation=abreviation)
    db.session.add(conference)
    db.session.commit()
    return conference.serialize()