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
    assert user.is_correct_password(DEFAULT_USER_DATA["password"])
    assert user.fullname == DEFAULT_USER_DATA["fullname"]
    assert user.photo == DEFAULT_USER_DATA["photo"]
    assert user.id == EXPECTED_USER_ID
    assert TIMESTAMP_1 < user.created_at < TIME_STAMP_2
    assert TIMESTAMP_1 < user.updated_at < TIME_STAMP_2


def test_user_update(init_db):
    user = UserRepository.save(User(**DEFAULT_USER_DATA))
    user_id = user.id
    user_creation_date = user.created_at
    new_data = {
        "fullname": "Jack Doe",
        "photo": "new photo.jpg",
        "email": "new@gmail",
        "password": "newpassword",
    }

    TIMESTAMP_1 = datetime.now()
    UserRepository.update(user_id, **new_data)
    TIME_STAMP_2 = datetime.now()

    user = UserRepository.load_by_id(user.id)

    assert user.email == new_data["email"]
    assert user.is_correct_password(new_data["password"])
    assert user.fullname == new_data["fullname"]
    assert user.photo == new_data["photo"]
    assert user.id == user_id
    assert user.created_at == user_creation_date
    assert TIMESTAMP_1 < user.updated_at < TIME_STAMP_2


def test_user_delete(init_db):
    user = UserRepository.save(User(**DEFAULT_USER_DATA))
    user_id = user.id
    user = UserRepository.delete(user_id)
    user = UserRepository.load_by_id(user_id)

    assert user is None
