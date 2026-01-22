import json
import csv
from typing import List, Dict, Any
from order_calculator import calculate_order


def build_product_map(products: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """
    Optimizes the product list into a dictionary for O(1) lookup.
    """
    return {p["productCode"]: p for p in products}


# Load json orders
with open("./orders.json") as f:
    orders = json.load(f)

# Load csv products
with open("./products.csv") as f:
    reader = csv.DictReader(f)
    products = list(reader)

product_map = build_product_map(products)
report = [calculate_order(order, product_map) for order in orders]

print(json.dumps(report, indent=2))
