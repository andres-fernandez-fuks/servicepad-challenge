import pytest
from project import create_app, db

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