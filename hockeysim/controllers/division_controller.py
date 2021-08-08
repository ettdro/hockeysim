from hockeysim.models.conference import Conference
from flask import Blueprint, render_template, session, abort, request, jsonify
from hockeysim.database import db
from hockeysim.models.division import Division

division_routes = Blueprint('division_routes', __name__)

@division_routes.route('/divisions/create', methods=['POST'])
def create():
    data = request.json
    name = data['name']
    abreviation = data['abreviation'] if 'abreviation' in data else None

    division = Division(name=name, abreviation=abreviation)
    division.conference = Conference.query.filter_by(id=data['conference_id']).first()
    db.session.add(division)
    db.session.commit()
    return division.serialize()
