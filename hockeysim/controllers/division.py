from flask import Blueprint, render_template, session, abort, request, jsonify
from hockeysim.database import db
from hockeysim.models.division import Division

division_routes = Blueprint('division_routes', __name__)
