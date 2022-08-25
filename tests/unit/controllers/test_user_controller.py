from project.controllers.user_controller import UserController
from project.helpers.request_helpers.user_helper import UserRequest


def test_user_creation(init_db):
    """
    Test create user
    """

    user_data = {
        "email": "example@gmail.com",
        "password": "password",
        "fullname": "John Doe",
        "photo": "photo.jpg",
    }

    user_request = UserRequest(**user_data)

    UserController.create_user(user_request)
    user = UserController.get_user_by_id(1)
    assert user.id == 1
    assert user.email == user_data["email"]
    assert user.is_correct_password(user_data["password"])
    assert user.fullname == user_data["fullname"]
    assert user.photo == user_data["photo"]


def test_user_obtention_by_id(init_db, saved_user):
    """
    Test get user by id
    """
    user = UserController.get_user_by_id(saved_user.id)
    assert user.id == saved_user.id
    assert user.email == saved_user.email
    assert user.fullname == saved_user.fullname
    assert user.photo == saved_user.photo
    assert user.created_at == saved_user.created_at
    assert user.updated_at == saved_user.updated_at


def test_user_update(init_db, saved_user):
    """
    Test update user
    """

    user_updated_date = saved_user.updated_at

    new_data = {
        "email": "new_email@gmail.com",
        "password": "new_password",
        "fullname": "new_fullname",
        "photo": "new_photo.jpg",
    }

    UserController.update_user(saved_user.id, new_data)
    user = UserController.get_user_by_id(saved_user.id)

    assert user.id == saved_user.id
    assert user.email == new_data["email"]
    assert user.is_correct_password(new_data["password"])
    assert user.fullname == new_data["fullname"]
    assert user.photo == new_data["photo"]
    assert user.created_at == saved_user.created_at
    assert user.updated_at > user_updated_date


def test_user_delete(init_db, saved_user):
    """
    Test delete user
    """

    UserController.delete_user(saved_user.id)
    user = UserController.get_user_by_id(saved_user.id)

    assert user is None

