from project.controllers.user_controller import UserController

def test_get_user_by_id(init_db, saved_user):
    """
    Test get user by id
    """
    user = UserController.get_user_by_id(saved_user.id)
    assert user.id == saved_user.id
    assert user.email == saved_user.email
    assert user.password == saved_user.password
    assert user.fullname == saved_user.fullname
    assert user.photo == saved_user.photo
    assert user.created_at == saved_user.created_at
    assert user.updated_at == saved_user.updated_at