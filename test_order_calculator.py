import pytest
from order_calculator import calculate_order


@pytest.fixture
def products():
    """
    A pre-prepared product list (dictionary) acting as the data source.
    This mimics the structure after the 'preparation' phase is complete.
    """
    return {
        "AAA": {"productCode": "AAA", "weight": "300", "price": "50"},
        "BBB": {"productCode": "BBB", "weight": "999", "price": "12"},
        "CCC": {"productCode": "CCC", "weight": "1000", "price": "168"},
    }


def test_calculate_total_with_quantity(products):
    """Verify quantity is multiplied by price correctly."""
    order = {"reference": "001", "items": [{"productCode": "AAA", "quantity": 3}]}

    # We pass the pre-prepared products directly to the calculator
    result = calculate_order(order, products)

    assert result["total"] == 150
    assert result["reference"] == "001"


def test_mixed_order_logic(products):
    """Verify logic works with multiple items in one order."""
    order = {
        "reference": "004",
        "items": [
            {"productCode": "AAA", "quantity": 2},  # Cost 100
            {"productCode": "BBB", "quantity": 1},  # Cost 12
        ],
    }
    result = calculate_order(order, products)

    assert result["total"] == 112


def test_unknown_product_ignored(products):
    """Ensure the calculator doesn't crash if a product is missing from the list."""
    order = {"reference": "005", "items": [{"productCode": "ZZZ", "quantity": 1}]}
    result = calculate_order(order, products)
    assert result["total"] == 0
