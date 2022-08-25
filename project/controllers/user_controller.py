from project.helpers.request_helpers.user_helper import UserRequest
from project.models.user import User
from project.repositories.user_repository import UserRepository

class UserController:

    @classmethod
    def get_user(cls, user_id):
        return UserRepository.load_by_id(user_id)

    @classmethod
    def create_user(cls, user_data):
        return UserRepository.save(User(**user_data))

    @classmethod
    def update_user(cls, id, data):
        user = UserRepository.load_by_id(id)
        user.update(**data)
        return user

    @classmethod
    def delete_user(cls, id):
        return UserRepository.delete(id)