from project.controllers.authentication_controller import AuthenticationController
from project.controllers.user_controller import UserController


def test_login(init_db, saved_user, saved_user_password):
    """
    Test login user
    """

    credentials = {"username": saved_user.email, "password": saved_user_password}
    AuthenticationController.login(credentials)
    user = UserController.get_user_by_id(saved_user.id)

    assert user.id == saved_user.id
    assert user.email == saved_user.email
    assert user.fullname == saved_user.fullname
    assert user.photo == saved_user.photo
    assert user.created_at == saved_user.created_at
    assert user.updated_at == saved_user.updated_at
    assert user.is_logged_in()


def test_logout(init_db, saved_user, saved_user_password):
    """
    Test logout user
    """

    credentials = {"username": saved_user.email, "password": saved_user_password}
    login_info = AuthenticationController.login(credentials)
    token = login_info["token"]
    user = UserController.get_user_by_id(saved_user.id)

    assert user.is_logged_in()  # to verify logout works, user must be logged in first

    AuthenticationController.logout(token)
    user = UserController.get_user_by_id(saved_user.id)

    assert not user.is_logged_in()
