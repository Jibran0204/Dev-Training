# Introduction

Here you will find a partial solution to a familiar looking challenge. The logic in the solution has been decoupled from the reporting element for improved seperation of concerns and ease of testing.

Your task is to extend out the tests in `test_order_calculator` to add test coverage for the free shipping part of the requirement. For testing, we are using the [ pytest](https://docs.pytest.org/en/stable/) library

You will then automate the running of these tests inside Github Actions, as well as automated code linting using [ruff](https://docs.astral.sh/ruff/linter/)

### To Do

- [ ] Create a new project on Github for your work:
  1. Create a new repository on GitHub. Do not initalise it.
  2. `git push **MY_REPO_URL** main:main`
  3. `cd..` out of this repository and delete it
  4. Clone your new repo to your machine
  5. Come back to these instructions

- [ ] Create a new virtual environment for your work and install the pytest module
- [ ] Run the tests

- [ ] Investigate how to run the tests as part of a CI/CD proccess in Github Actions

- [ ] Consider the specification below. Extend the tests to cover the missing functionality (https://en.wikipedia.org/wiki/Test-driven_development)
- [ ] Push the new 'broken' tests to Github, and see your Github Action fail
- [ ] Write the missing code to fix the tests
- [ ] Push to github and see you tests pass

- [ ] Investigate the code linting tool `ruff`
- [ ] Fix any `ruff check` failures
- [ ] Fix any `ruff format` formatting issues

- [ ] Investigate how `uv` can make managing virtual environments easier.

---

### **Function Specification:** calculate_order

### 1. Overview

The calculate_order function processes a single customer order against a dataset of available products. Its responsibility is to calculate the total cost of the order and determine if the customer qualifies for free shipping based on specific business rules.

### 2. Signature

```Python

def calculate_order(order: dict, products: dict) -> dict:
```

### 3. Inputs

`order` (dict)

A dictionary representing a single customer order.

**Structure:**

```JSON

    {
      "reference": "String (Order ID)",
      "items": [
        {
          "productCode": "String (matches product lookup key)",
          "quantity": "Integer (Number of units ordered)"
        }
      ]
    }
```

`products` (dict)

A pre-processed lookup dictionary where keys are product codes.

**Structure:**

```JSON

    {
      "product_code": {
        "productCode": "String",
        "price": "Integer or String (representing an integer)",
        "weight": "Integer or String (representing an integer)"
      }
    }
```

_Note_: The function must gracefully handle price and weight values passed as strings (e.g., "50"), casting them to integers internally.

### 4. Output

Returns a dictionary representing the finalized report for that order.

**Structure:**

```JSON

    {
      "reference": "String (Passed through from input)",
      "total": "Integer (Calculated total cost)",
      "freeShipping": "Boolean"
    }
```

### 5. Logic & Business Rules

#### A. Total Calculation

Iterate through the list of items in the order.

Retrieve the corresponding product details from the products map using productCode.

If the product exists:

- Parse price to an integer.

- Calculate line cost: price \* quantity.

- Add line cost to the running total.

If a product code is not found in the products map, it should be ignored (or treated as price 0).

#### B. Free Shipping Eligibility

An order qualifies for freeShipping: true only if both of the following conditions are met:

- Minimum Spend: The calculated total is strictly greater than 100 (total > 100).

- Weight Limit: The order does not contain any single item type with a unit weight of 1000 or more (weight < 1000).

- Note: This check applies to the individual unit weight of the product, not the combined weight of the quantity ordered.

### 6. Edge Case Handling

- Data Types: The function must assume products data may come from CSV (strings) and safely cast numerical values to int before calculation.

- Missing Items: If an order contains an items list that is empty, the total should be 0 and free shipping false.

- Missing Product Code: If an item in the order references a productCode not found in the products dictionary, that item should not contribute to the total or weight checks.
