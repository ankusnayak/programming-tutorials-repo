import pytest
from source.service import UserService, APIClient


def test_get_username_with_mock(mocker):
    """
        We only test this class UserService. without relay on APIClient
        works properly or not. So mock APIClient.
    """
    # Mock an entire class APIClient
    mock_api_client = mocker.Mock(spec=APIClient)  # Create a mock API client

    # Mock get_user_data to return fake user
    mock_api_client.get_user_data.return_value = {"id": 1,
                                                  "name": "Ankus"}
    
    service = UserService(mock_api_client)

    # Call method that depends on the mock
    result = service.get_username(1)

    # Assertions
    assert result == "ANKUS"  # Check if processing was done correctly

    # Ensure correct API call
    mock_api_client.get_user_data.assert_called_once_with(1)
