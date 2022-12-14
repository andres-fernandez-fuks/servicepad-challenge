from datetime import datetime
from unittest.mock import DEFAULT
from project.repositories.publication_repository import PublicationRepository
from project.models.publication import Publication

DEFAULT_PUBLICATION_DATA = {
    "title": "Example Publication",
    "description": "Example Publication Description",
    "priority": "High",
    "status": "open",
}


def create_publication(user_id):
    publication_data = DEFAULT_PUBLICATION_DATA.copy()
    publication_data["user_id"] = user_id
    return PublicationRepository.save(Publication(**publication_data))


def test_publication_creation(init_db, saved_user):
    EXPECTED_PUBLICATION_ID = len(PublicationRepository.load_all()) + 1

    TIMESTAMP_1 = datetime.now()
    publication = create_publication(saved_user.id)
    TIME_STAMP_2 = datetime.now()

    publication = PublicationRepository.load_by_id(publication.id)

    assert publication.id == EXPECTED_PUBLICATION_ID
    assert publication.title == DEFAULT_PUBLICATION_DATA["title"]
    assert publication.description == DEFAULT_PUBLICATION_DATA["description"]
    assert publication.priority == DEFAULT_PUBLICATION_DATA["priority"]
    assert publication.status == DEFAULT_PUBLICATION_DATA["status"]
    assert publication.user.id == saved_user.id
    assert publication.user.email == saved_user.email
    assert publication.user.fullname == saved_user.fullname
    assert publication.user.photo == saved_user.photo
    assert TIMESTAMP_1 < publication.created_at < TIME_STAMP_2
    assert TIMESTAMP_1 < publication.updated_at < TIME_STAMP_2


def test_publication_update(init_db, saved_user):
    publication = create_publication(saved_user.id)

    new_data = {
        "title": "New Example Publication",
        "description": "New Example Publication Description",
        "priority": "Low",
        "status": "closed",
    }
    TIMESTAMP_1 = datetime.now()
    PublicationRepository.update(publication.id, **new_data)
    TIME_STAMP_2 = datetime.now()
    publication = PublicationRepository.load_by_id(publication.id)

    assert publication.title == new_data["title"]
    assert publication.description == new_data["description"]
    assert publication.priority == new_data["priority"]
    assert publication.status == new_data["status"]
    assert publication.user.id == saved_user.id
    assert TIMESTAMP_1 < publication.updated_at < TIME_STAMP_2


def test_publication_delete(init_db, saved_user):
    publication = create_publication(saved_user.id)
    publication_id = publication.id
    publication = PublicationRepository.delete(publication_id)
    publication = PublicationRepository.load_by_id(publication_id)

    assert publication is None

