from source.weather import get_weather


def test_get_weather():
    assert get_weather(21) == "hot"
    assert get_weather(20) == "cold"
