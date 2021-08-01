from hockeysim.models import User


def test_user_register(client):
    response = client.post(
        '/register', json={'username': 'username', 'email': 'email@gmail.com'})
    assert response.status_code == 200

    user = User.query.filter_by(username='username').first()
    assert user != None
    assert response.json['username'] == 'username'
