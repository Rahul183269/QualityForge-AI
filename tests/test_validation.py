import pytest
from src.validation import is_valid_quantity
from src.validation import is_valid_price
from src.validation import is_success

@pytest.mark.parametrize(
    "quantity, expected",
    [
        (0, False),
        (1, True),
        (2, True),
        (99, True),
        (100, True),
        (101, False),
    ]
)
def test_quantity_boundaries(quantity, expected):
    assert is_valid_quantity(quantity) is expected


@pytest.mark.parametrize(
    "price, expected",
    [
        (99, False),
        (100, True),
        (101, True),
        (9999, True),
        (10000, True),
        (10001, False),
    ]
)
def test_price_boundaries(price, expected):
    assert is_valid_price(price) is expected




@pytest.mark.parametrize(
    "status_code, expected",
    [
        (200, True),
        (201, True),
        (204, True),
        (299, True),
        (300, False),
        (404, False),
        (500, False),
    ],
)
def test_is_success(status_code, expected):
    assert is_success(status_code) is expected