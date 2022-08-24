from project.exceptions.ownership_exception import OwnershipException
from project.models.publication import Publication
from project.repositories.publication_repository import PublicationRepository
from project.repositories.user_repository import UserRepository


class PublicationController:
    @classmethod
    def get_all_user_publications(cls, user_id):
        return PublicationRepository.load_all_from_user(user_id)

    @classmethod
    def get_publication_by_id(cls, user_id, publication_id):
        cls.validate_ownership(user_id, publication_id)
        return PublicationRepository.load_by_id(publication_id)

    @classmethod
    def create_publication(cls, user_id, data):
        publication = Publication(user_id=user_id, **data)
        return PublicationRepository.save(publication)

    @classmethod
    def update_publication(cls, user_id, publication_id, data):
        cls.validate_ownership(user_id, publication_id)
        publication = PublicationRepository.load_by_id(publication_id)
        publication.update(**data)
        return PublicationRepository.save(publication)

    @classmethod
    def delete_publication(cls, user_id, publication_id):
        cls.validate_ownership(user_id, publication_id)
        return PublicationRepository.delete(publication_id)

    @classmethod
    def validate_ownership(cls, user_id, publication_id):
        user = UserRepository.load_by_id(user_id)
        publication = PublicationRepository.load_by_id(publication_id)
        if not user or not publication or user.id != publication.user_id:
            raise OwnershipException()
