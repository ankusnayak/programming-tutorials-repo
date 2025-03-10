import pytest
from source.main import UserManager


@pytest.fixture
def user_manager():
    """Creates a fresh instance of UserManager before each test.
        This is kind of setup step before each test.
        fixture -> will run every time before every test runs.
    """
    return UserManager()


def test_add_user(user_manager):
    assert user_manager.add_user("ankus_nayak", "ankus@example.com") == True
    assert user_manager.get_user("ankus_nayak") == "ankus@example.com"


def test_add_duplicate_user(user_manager):
    user_manager.add_user("ankus_nayak", "ankus@example.com")
    with pytest.raises(ValueError):
        user_manager.add_user("ankus_nayak", "ankus@example.com")
