from typing import Any, Dict, List


def calculate_order(
    order: Dict[str, Any], product_map: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Processes a SINGLE order.
    This is the most important function to test.
    """
    total_price = 0
    has_heavy_item = False
    free_shipping = False

    # Iterate through items in this specific order
    for item in order.get("items", []):
        p_code = item["productCode"]
        quantity = item["quantity"]

        product = product_map.get(p_code)

        if product:
            # Cast strings to integers
            price = int(product["price"])
            weight = int(product["weight"])

            total_price += price * quantity

            if weight >= 1000:
                has_heavy_item = True

    # Business Rules
    # Free shipping only if total price exceeds 100 and has heavy item
    if total_price > 100 and has_heavy_item:
        free_shipping = True

    return {
        "reference": order["reference"],
        "total": total_price,
        "freeShipping": free_shipping,
    }
