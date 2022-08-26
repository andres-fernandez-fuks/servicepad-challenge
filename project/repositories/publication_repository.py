from project.repositories.base_repository import BaseRepository
from project.models.publication import Publication

class PublicationRepository(BaseRepository):
    """
    Publication repository. Handles the persistence of the publications in the database.
    """
    object_class = Publication