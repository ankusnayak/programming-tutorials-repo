import pytest
from source.api_test import app


@pytest.fixture
def client():
    """provides a test client for the Flask app."""
    app.config['TESTING'] = True  # Enable testing mode

    with app.test_client() as client:
        yield client


def test_add_user(client):
    """Test adding a new user."""
    response = client.post('/users', json={"id": 1, "name": "Ankus"})

    assert response.status_code == 201
    assert response.json == {"id": 1, "name": "Ankus"}


def test_get_user(client):
    """Test retrieving a user."""

    # First, add a user
    client.post('/users', json={"id": 2, "name": "Ankan"})

    # Then, retrieve the user by passing client_id which data we want to get
    response = client.get('/users/2')
    assert response.status_code == 200
    assert response.json == {"id": 2, "name": "Ankan"}


def test_get_user_not_found(client):
    response = client.get('/users/100')

    assert response.status_code == 404
    assert response.json == {"error": "User not found"}


def test_add_duplicate_user(client):
    """Test adding a duplicate user."""
    client.post('/users', json={"id": 3, "name": "Sumita"})

    response = client.post('/users', json={"id": 3, "name": "Sumita"})
    assert response.status_code == 400
