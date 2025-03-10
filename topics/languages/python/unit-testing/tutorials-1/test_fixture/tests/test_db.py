import pytest
from source.db import Database


@pytest.fixture
def db():
    """Provides a fresh instance of Database class and
        cleans up after the test. TearDown in simple terms.
    """
    database = Database()
    yield database

    # Cleanup step (not needed for in-memory, but useful for real DBs)
    database.data.clear()


def test_add_user(db):

    db.add_user(1, "Ankus")
    assert db.get_user(1) == "Ankus"


def test_add_duplicate_user(db):
    db.add_user(1, "Ankan")

    # Handle Exception
    with pytest.raises(ValueError, match='User already exists'):
        db.add_user(1, "Ankan")


def test_delete_user(db):
    db.add_user(2, "Sayan")
    db.delete_user(2)

    assert db.get_user(2) is None
