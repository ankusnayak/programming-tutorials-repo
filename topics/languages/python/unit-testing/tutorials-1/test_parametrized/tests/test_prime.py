import pytest
from source.prime import is_prime


# Parameterized Testing
@pytest.mark.parametrize("num, expected", [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (17, True)
])
def test_is_prime(num, expected):
    assert is_prime(num) == expected
