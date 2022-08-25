import pytest
from project import create_app, db
from project.models.publication import Publication
from project.models.user import User


@pytest.fixture(scope="function")
def test_client():
    app = create_app(test_mode=True)
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


@pytest.fixture(scope="function")
def init_db(test_client):
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()


@pytest.fixture(scope="function")
def _db():
    return db


@pytest.fixture(scope="function")
def saved_user_password():
    return "password"


@pytest.fixture(scope="function")
def saved_user(init_db, _db):
    user = User(
        email="example@gmail.com",
        password="password",
        fullname="John Doe",
        photo="image.jpg",
    )
    user.logged_in = True  # needed for authentication purposes
    _db.session.add(user)
    _db.session.commit()
    return user


@pytest.fixture(scope="function")
def saved_publication(init_db, _db, saved_user):
    publication = Publication(
        title="Publication title",
        description="Publication description",
        priority="High",
        user_id=saved_user.id,
        status="status",
    )
    _db.session.add(publication)
    _db.session.commit()
    return publication
