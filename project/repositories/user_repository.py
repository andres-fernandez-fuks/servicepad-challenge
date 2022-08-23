from project.repositories.base_repository import BaseRepository
from project.models.user import User


class UserRepository(BaseRepository):
    object_class = User