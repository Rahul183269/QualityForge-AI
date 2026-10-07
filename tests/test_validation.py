import pytest
from src.validation import is_valid_quantity
from src.validation import is_valid_price

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

