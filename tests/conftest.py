import pytest
from project import create_app

@pytest.fixture(scope="function")
def test_client():
    app = create_app(test_mode=True)
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client 