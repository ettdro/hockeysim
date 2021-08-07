from flask import Blueprint, render_template, session, abort, request, jsonify
from hockeysim.database import db
from hockeysim.models.conference import Conference

conference_routes = Blueprint('conference_routes', __name__)
