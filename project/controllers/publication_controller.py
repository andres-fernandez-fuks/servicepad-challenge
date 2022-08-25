from project.exceptions.exceptions import AuthenticationException, ObjectNotFoundException, OwnershipException
from project.models.publication import Publication
from project.repositories.publication_repository import PublicationRepository
from project.repositories.user_repository import UserRepository


class PublicationController:
    @classmethod
    def get_all_user_publications(cls, user_id):
        return PublicationRepository.load_all_from_user(user_id)

    @classmethod
    def get_user_publication(cls, user_id, publication_id):
        cls.validate_ownership(user_id, publication_id)
        return PublicationRepository.load_by_id(publication_id)

    @classmethod
    def create_publication(cls, user_id, publication_data):
        publication = Publication(user_id=user_id, **publication_data)
        return PublicationRepository.save(publication)

    @classmethod
    def update_publication(cls, user_id, publication_id, publication_new_data):
        cls.validate_ownership(user_id, publication_id)
        publication = PublicationRepository.load_by_id(publication_id)
        publication.update(**publication_new_data)
        return PublicationRepository.save(publication)

    @classmethod
    def delete_publication(cls, user_id, publication_id):
        cls.validate_ownership(user_id, publication_id)
        PublicationRepository.delete(publication_id)

    @classmethod
    def validate_ownership(cls, user_id, publication_id):
        publication = PublicationRepository.load_by_id(publication_id)
        if not publication:
            raise ObjectNotFoundException("publication", publication_id)
        user = UserRepository.load_by_id(user_id)
        if not user:
            raise ObjectNotFoundException("user", user_id)
        if user.id != publication.user_id:
            raise OwnershipException()
        if not user.is_logged_in():
            raise AuthenticationException()       
