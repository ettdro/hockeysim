from hockeysim.seeders.conferences import ConferenceSeeder
from hockeysim.seeders.divisions import DivisionSeeder
from hockeysim.seeders.teams import TeamSeeder
from flask.cli import with_appcontext
from flask import current_app

import click

def init_seeder():
    current_app.cli.add_command(populate)


@click.command("populate")
@with_appcontext
def populate():
    """Seeds the database"""
    seeders = [ConferenceSeeder(), DivisionSeeder(), TeamSeeder()]
    for s in seeders:
        s.run()
        click.echo("Seed for {} completed".format(s.__class__.__name__))
