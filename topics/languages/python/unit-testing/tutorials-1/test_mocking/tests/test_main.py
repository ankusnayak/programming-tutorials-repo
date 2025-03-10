import pytest
from source.main import get_weather


def test_get_weather(mocker):
    # This mocker will work because we have install pytest mocker \
    # library while install pytest.

    # Mock request.get

    # Patch a specific function -- Mock function
    mock_get = mocker.patch("example_4_mock.requests.get")

    # mock status code
    mock_get.return_value.status_code = 200

    # json is function so access the return_value
    mock_get.return_value.json.return_value = {"temperature": 25,
                                               "condition": "Sunny"}

    # Call function
    result = get_weather("Contai")

    # Assertions
    assert result == {"temperature": 25, "condition": "Sunny"}

    # Check if mock_get gets called
    mock_get.assert_called_once_with("https://api.weather.com/v1/Contai")
