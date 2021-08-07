from sqlalchemy.sql.expression import false
from hockeysim.models.conference import Conference
import json
from tests.conftest import create_conference


def test_conference_serialize_returns_dictionary(client):
    name = 'East'
    abreviation = 'EAST'
    response = create_conference(
        client, {'name': name, 'abreviation': abreviation})
    assert response.status_code == 200

    conference = Conference.query.filter_by(name=name).first()
    assert conference is not None
    assert conference.serialize() == json.loads(response.data)


def test_conference_serialize_contains_all_columns(client):
    name = 'East'
    abreviation = 'EAST'
    response = create_conference(
        client, {'name': name, 'abreviation': abreviation})
    assert response.status_code == 200

    conference = Conference.query.filter_by(name=name).first()
    conference_serialized = conference.serialize()
    for column in Conference.__table__.columns:
        assert column.name in conference_serialized


def test_conference_no_abreviation_sets_automatically(client):
    name = 'East'
    response = create_conference(client, {'name': name})
    assert response.status_code == 200

    conference = Conference.query.filter_by(name=name).first()
    assert conference is not None
    assert conference.abreviation == 'EAST'
    assert conference.serialize() == json.loads(response.data)


def test_conference_repr_returns_good_format():
    assert repr(Conference(name="East")) == "<Conference(id=None,name='East',abreviation='EAST',created_at=None,updated_at=None)>"