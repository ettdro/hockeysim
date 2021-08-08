from flask_sqlalchemy import SQLAlchemy
from flask import current_app
from flask.cli import with_appcontext

import click

db = SQLAlchemy()

Column = db.Column
Model = db.Model


def init_db():
    db.init_app(current_app)
    current_app.cli.add_command(migrate)


@click.command("migrate")
@with_appcontext
def migrate():
    """Clear existing data and create new tables."""
    init_db()
    db.create_all()
    click.echo("Migration completed")
