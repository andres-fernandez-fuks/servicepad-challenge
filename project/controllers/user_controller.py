from project.models.user import User
from project.repositories.user_repository import UserRepository

class UserController:

    @classmethod
    def get_user_by_id(cls, id):
        return UserRepository.load_by_id(id)

    @classmethod
    def create_user(cls, data):
        return UserRepository.save(User(**data.dict()))

    @classmethod
    def update_user(cls, id, data):
        user = UserRepository.load_by_id(id)
        user.update(**data)
        return user

    @classmethod
    def delete_user(cls, id):
        return UserRepository.delete(id)