from project.repositories.base_repository import BaseRepository
from project.models.publication import Publication

class PublicationRepository(BaseRepository):
    object_class = Publication