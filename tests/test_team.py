from hockeysim.models.team import Team
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

    assert team is not None and team.name == name and team.city == city


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


def test_team_serialize_returns_dictionary(client):
    response = create_team(client, {'name': 'Name', 'city': 'City'})
    assert response.status_code == 200
    
    team = Team.query.filter_by(name='Name').first()
    assert team.serialize() == json.loads(response.data)


def test_team_repr_returns_good_format():
    assert repr(Team(id=1)) == '<Team(id=1,city=None,name=None,abreviation=None,division=None,created_at=None,updated_at=None)>'


'''def test_create_team_must_have_a_division(client, mock_division, mock_get_sqlalchemy, mock_division_id):
    mock_get_sqlalchemy.filter_by.return_value = mock_division
    city = 'Montreal'
    name = 'Canadiens'
    response = create_team(client, {'name': name, 'city': city})
    assert response.status_code == 200
    # team = Team.query.filter_by(name=name, city=city).first()'''
