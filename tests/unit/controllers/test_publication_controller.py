from project.controllers.publication_controller import PublicationController
from project.repositories.publication_repository import PublicationRepository


def test_publication_creation(init_db, saved_user):
    """
    Test create publication
    """

    publication_data = {
        "title": "title",
        "description": "description",
        "priority": "priority",
        "status": "status",
    }

    publication = PublicationController.create_publication(
        saved_user.id, publication_data
    )
    publication = PublicationRepository.load_by_id(publication.id)
    assert publication.id == 1
    assert publication.title == publication_data["title"]
    assert publication.description == publication_data["description"]
    assert publication.priority == publication_data["priority"]
    assert publication.status == publication_data["status"]
    assert publication.user.id == saved_user.id


def test_publication_obtention_by_id(init_db, saved_user, saved_publication):
    """
    Test get publication by id
    """
    publication = PublicationController.get_publication_by_id(
        saved_user.id, saved_publication.id
    )
    assert publication.id == saved_publication.id
    assert publication.title == saved_publication.title
    assert publication.description == saved_publication.description
    assert publication.priority == saved_publication.priority
    assert publication.status == saved_publication.status
    assert publication.user == saved_user
    assert publication.created_at == saved_publication.created_at
    assert publication.updated_at == saved_publication.updated_at


def test_publication_update(init_db, saved_user, saved_publication):
    """
    Test update publication
    """

    publication_updated_date = saved_user.updated_at

    new_data = {
        "title": "new_title",
        "description": "new_description",
        "priority": "new_priority",
        "status": "new_status",
    }

    PublicationController.update_publication(
        saved_user.id, saved_publication.id, new_data
    )
    publication = PublicationRepository.load_by_id(saved_publication.id)

    assert publication.id == saved_publication.id
    assert publication.title == new_data["title"]
    assert publication.description == new_data["description"]
    assert publication.priority == new_data["priority"]
    assert publication.status == new_data["status"]
    assert publication.user == saved_user
    assert publication.updated_at > publication_updated_date


def test_publication_delete(init_db, saved_user, saved_publication):
    """
    Test delete publication
    """

    PublicationController.delete_publication(saved_user.id, saved_publication.id)
    publication = PublicationRepository.load_by_id(saved_publication.id)
    assert publication is None
