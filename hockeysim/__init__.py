from hockeysim.config import DevConfig, TestConfig
from flask import Flask
from .database import init_db
from .seeder import init_seeder

def create_app(testing=False):
    app = Flask(__name__)
    if testing:
        app.config.from_object(TestConfig)
    else:
        app.config.from_object(DevConfig)

    with app.app_context():
        init_db()
        init_seeder()

    from hockeysim.controllers.conference_controller import conference_routes
    from hockeysim.controllers.division_controller import division_routes
    from hockeysim.controllers.user_controller import user_routes
    from hockeysim.controllers.team_controller import team_routes

    app.register_blueprint(conference_routes)
    app.register_blueprint(division_routes)
    app.register_blueprint(user_routes)
    app.register_blueprint(team_routes)

    return app
