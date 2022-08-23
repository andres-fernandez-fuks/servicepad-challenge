from datetime import datetime
from project.repositories.user_repository import UserRepository
from project.models.user import User

def test_user_creation(init_db):
    EXPECTED_USER_ID = len(UserRepository.load_all()) + 1
    TIMESTAMP_1 = datetime.now()

    user_data = {
        'email': 'example@mail.com',
        'password': 'password',
        'fullname': 'John Doe',
        'photo': 'https://example.com/photo.jpg'
    }
    user = UserRepository.save(User(**user_data))
    TIME_STAMP_2 = datetime.now()

    assert user.email == user_data['email']
    assert user.password == user_data['password']
    assert user.fullname == user_data['fullname']
    assert user.photo == user_data['photo']
    assert user.id == EXPECTED_USER_ID
    assert TIMESTAMP_1 < user.created_at < TIME_STAMP_2
    assert TIMESTAMP_1 < user.updated_at < TIME_STAMP_2
