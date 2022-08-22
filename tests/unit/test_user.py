from project.models.user import User

def test_user_creation(test_client):
    user_data = {
        'email': 'example@mail.com',
        'password': 'password',
        'fullname': 'John Doe',
        'photo': 'https://example.com/photo.jpg'
    }
    user = User(**user_data)
    assert user.email == user_data['email']
    assert user.password == user_data['password']
    assert user.fullname == user_data['fullname']
    assert user.photo == user_data['photo']