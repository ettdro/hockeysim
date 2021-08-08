from hockeysim.models.conference import Conference
from hockeysim.models.division import Division
from hockeysim.models.team import Team
from tests.conftest import create_conference, create_division
import json


def create_team(client, json):
    response = client.post('/teams/create', json=json)
    return response


def test_create_team(client):
    name = 'Ducks'
    city = 'Anaheim'
    response = create_team(client, {'name': name, 'city': city})
    assert response.status_code == 200

    team = Team.query.filter_by(name=name).first()

    assert team is not None
    assert team.name == name
    assert team.city == city
    assert team.abreviation == city.upper()[0:3]


def test_create_team_with_empty_city_and_name(client):
    name = ''
    response = create_team(client, {'name': name, 'city': ''})

    assert Team.query.filter_by(name=name).first() is None
    assert response.status_code == 500


def test_create_team_with_empty_city_or_name(client):
    city = 'Montreal'
    response = create_team(client, {'name': '', 'city': city})

    assert Team.query.filter_by(city=city).first() is None
    assert response.status_code == 500


def test_create_team_with_city_name_and_abreviation(client):
    city = 'Montreal'
    name = 'Canadiens'
    abreviation = 'MTL'
    response = create_team(client, {'name': name, 'city': city, 'abreviation': abreviation})
    assert response.status_code == 200

    team = Team.query.filter_by(city=city).first()

    assert team is not None
    assert team.name == name
    assert team.city == city
    assert team.abreviation == abreviation


def test_create_team_has_conference(client):
    create_conference(client, {'name': 'East'})
    conference = Conference.query.filter_by(name='East').first()

    create_division(client, {'name': 'Atlantic', 'conference_id': conference.id})
    division = Division.query.filter_by(name='Atlantic').first()

    response = create_team(client, {'name': 'Name', 'city': 'City'})
    assert response.status_code == 200

    team = Team.query.filter_by(name='Name').first()
    team.division = division
    team.save()

    assert team.division == division
    assert team.division.conference == conference


def test_team_serialize_returns_dictionary(client):
    response = create_team(client, {'name': 'Name', 'city': 'City'})
    assert response.status_code == 200
    
    team = Team.query.filter_by(name='Name').first()
    assert team.serialize() == json.loads(response.data)


def test_team_repr_returns_good_format():
    assert repr(Team(name='Canadiens', city='Montreal')) == "<Team(id=None,city='Montreal',name='Canadiens',abreviation='MON',division=None,created_at=None,updated_at=None)>"


'''def test_create_team_must_have_a_division(client, mock_division, mock_get_sqlalchemy, mock_division_id):
    mock_get_sqlalchemy.filter_by.return_value = mock_division
    city = 'Montreal'
    name = 'Canadiens'
    response = create_team(client, {'name': name, 'city': city})
    assert response.status_code == 200
    # team = Team.query.filter_by(name=name, city=city).first()'''
