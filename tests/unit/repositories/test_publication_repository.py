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


def test_publication_creation(init_db, saved_user):
    EXPECTED_PUBLICATION_ID = len(PublicationRepository.load_all()) + 1
    publication_data = DEFAULT_PUBLICATION_DATA.copy()
    publication_data["user_id"] = saved_user.id
    TIMESTAMP_1 = datetime.now()

    publication = PublicationRepository.save(Publication(**publication_data))
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
    original_data = DEFAULT_PUBLICATION_DATA.copy()
    original_data["user_id"] = saved_user.id
    publication = PublicationRepository.save(Publication(**original_data))

    new_data = {key: f"New {value}" for key, value in DEFAULT_PUBLICATION_DATA.items()}
    TIMESTAMP_1 = datetime.now()
    publication.update(**new_data)
    TIME_STAMP_2 = datetime.now()
    publication = PublicationRepository.load_by_id(publication.id)

    assert publication.title == "New " + DEFAULT_PUBLICATION_DATA["title"]
    assert publication.description == "New " + DEFAULT_PUBLICATION_DATA["description"]
    assert publication.priority == "New " + DEFAULT_PUBLICATION_DATA["priority"]
    assert publication.status == "New " + DEFAULT_PUBLICATION_DATA["status"]
    assert publication.user.id == saved_user.id
    assert TIMESTAMP_1 < publication.updated_at < TIME_STAMP_2

