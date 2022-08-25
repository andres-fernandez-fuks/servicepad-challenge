from project.repositories.base_repository import BaseRepository
from project.models.user import User


class UserRepository(BaseRepository):
    object_class = User

    @classmethod
    def load_by_email(cls, email: str):
        return cls.load_by_field("email", email)

    @classmethod
    def login(cls, user: User):
        user.login()
        cls.save(user)

    @classmethod
    def logout(cls, user: User):
        user.logout()
        cls.save(user)
