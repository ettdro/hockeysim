import json
from hockeysim.models.user import User


def test_user_register(client):
    response = client.post(
        '/register', json={'username': 'username', 'email': 'email@gmail.com'})
    assert response.status_code == 200

    user = User.query.filter_by(username='username').first()
    assert user != None
    assert response.json['username'] == 'username'


def test_team_serialize_returns_dictionary(client):
    response = client.post(
        '/register', json={'username': 'username', 'email': 'email@gmail.com'})
    assert response.status_code == 200

    user = User.query.filter_by(username='username').first()
    assert user.serialize() == json.loads(response.data)


def test_user_repr_returns_good_format():
    assert repr(User(
        id=1)) == '<User(id=1,username=None,email=None,created_at=None,updated_at=None)>'
