from datetime import datetime
from project.repositories.user_repository import UserRepository
from project.models.user import User

DEFAULT_USER_DATA = {
    "email": "example@gmail.com",
    "password": "password",
    "fullname": "John Doe",
    "photo": "photo.jpg",
}


def test_user_creation(init_db):
    EXPECTED_USER_ID = len(UserRepository.load_all()) + 1
    TIMESTAMP_1 = datetime.now()

    user = UserRepository.save(User(**DEFAULT_USER_DATA))
    TIME_STAMP_2 = datetime.now()

    user = UserRepository.load_by_id(user.id)

    assert user.email == DEFAULT_USER_DATA["email"]
    assert user.password == DEFAULT_USER_DATA["password"]
    assert user.fullname == DEFAULT_USER_DATA["fullname"]
    assert user.photo == DEFAULT_USER_DATA["photo"]
    assert user.id == EXPECTED_USER_ID
    assert TIMESTAMP_1 < user.created_at < TIME_STAMP_2 # cannot test for specific value
    assert TIMESTAMP_1 < user.updated_at < TIME_STAMP_2  # cannot test for specific value


def test_user_update(init_db):
    user = UserRepository.save(User(**DEFAULT_USER_DATA))
    user_id = user.id
    user_creation_date = user.created_at
    new_data = {key: f"new_{value}" for key, value in DEFAULT_USER_DATA.items()}

    TIMESTAMP_1 = datetime.now()
    user.update(**new_data)
    TIME_STAMP_2 = datetime.now()

    user = UserRepository.load_by_id(user.id)

    assert user.email == "new_" + DEFAULT_USER_DATA["email"]
    assert user.password == "new_" + DEFAULT_USER_DATA["password"]
    assert user.fullname == "new_" + DEFAULT_USER_DATA["fullname"]
    assert user.photo == "new_" + DEFAULT_USER_DATA["photo"]
    assert user.id == user_id
    assert user.created_at == user_creation_date
    assert TIMESTAMP_1 < user.updated_at < TIME_STAMP_2


def test_user_delete(init_db):
    user = UserRepository.save(User(**DEFAULT_USER_DATA))
    user_id = user.id
    user = UserRepository.delete(user)
    user = UserRepository.load_by_id(user_id)

    assert user is None