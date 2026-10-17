def is_valid_quantity(quantity: int) -> bool:
    return 1 <= quantity <= 100


def is_valid_price(price: int) -> bool:
    return 100 <= price <= 10000

def is_success(status_code: int) -> bool:
    return 200 <= status_code < 300