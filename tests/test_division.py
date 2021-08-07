from hockeysim.models.division import Division
from hockeysim.models.conference import Conference
from tests.conftest import create_conference, create_division

def test_create_division_with_conference(client):
    response_conference = create_conference(client, {'name': 'East'})
    assert response_conference == 200

    conference = Conference.query.filter_by(name='East').first()
    response_division = create_division(
        client, {'name': 'Atlantic', 'abreviation': 'ATL', 'conference_id': conference.id})
    
    assert response_division.status_code == 200

    division = Division.query.filter_by(name='Atlantic').first()
    assert division is not None
    assert division.conference.id == conference.id
    assert division.conference != None


def test_division_repr_returns_good_format():
    assert repr(Division(name="Atlantic")) == "<Division(id=None,name='Atlantic',conference=None,abreviation='ATL',created_at=None,updated_at=None)>"
