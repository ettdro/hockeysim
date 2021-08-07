from flask import Blueprint, render_template, session, abort, request, jsonify
from hockeysim.database import db
from hockeysim.models.team import Team

team_routes = Blueprint('team_routes', __name__)


@team_routes.route('/teams/create', methods=['POST'])
def create():
    data = request.json
    name = data['name']
    city = data['city']

    if (name == '' or city == ''):
        return "Name or city can't be empty", 500

    team = Team(name=name, city=city)
    db.session.add(team)
    db.session.commit()
    return team.serialize()
