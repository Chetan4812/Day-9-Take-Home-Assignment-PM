"""
FROZENSET BUNDLES MODULE

1️⃣ What is a frozenset?

A frozenset is an immutable version of a Python set. Once created,
its elements cannot be modified — meaning you cannot add, remove,
or update items.

Example:
fs = frozenset([1,2,3])

fs.add(4)  ❌ Not allowed


2️⃣ Difference Between set and frozenset

set
----
• Mutable
• Elements can be added or removed
• Cannot be used as dictionary keys
• Slightly faster for modifications

frozenset
---------
• Immutable
• Cannot be modified after creation
• Hashable → Can be used as dictionary keys
• Safer for fixed collections


3️⃣ When to Use frozenset in Real Systems

frozensets are useful when the collection of elements must remain fixed.

Common real-world uses:

• Dictionary keys for combinations
  Example: product bundle discounts

• Caching systems
  (e.g., caching results for combinations of filters)

• Graph algorithms where edges should not mutate

• Permission systems where roles should remain fixed

• Configuration rules

In this example, we use frozenset to represent product category bundles
because bundle definitions should not change once created.
"""

from collections import namedtuple
import timeit


# --------------------------------------------------
# Product Model
# --------------------------------------------------

Product = namedtuple("Product", ["id", "name", "category", "price"])


# --------------------------------------------------
# Sample Products
# --------------------------------------------------

laptop = Product(1, "Laptop", "Electronics", 75000)
phone = Product(2, "Smartphone", "Electronics", 50000)
clean_code = Product(3, "Clean Code", "Books", 500)
python_book = Product(4, "Python Crash Course", "Books", 700)
tshirt = Product(5, "T-Shirt", "Clothing", 800)
chair = Product(6, "Office Chair", "Home", 7000)


# --------------------------------------------------
# Example Cart
# --------------------------------------------------

customer_cart = {laptop, clean_code, tshirt}


# --------------------------------------------------
# 2️⃣ Bundle Discount System
# --------------------------------------------------

bundle_discounts = {

    frozenset({"Electronics", "Books"}): 10,
    frozenset({"Electronics", "Clothing"}): 5,
    frozenset({"Books", "Home"}): 7,
    frozenset({"Electronics", "Books", "Home"}): 15
}


# --------------------------------------------------
# 3️⃣ Bundle Checker Function
# --------------------------------------------------

def check_bundle_discount(cart):
    """
    Checks if cart qualifies for bundle discounts.

    Steps:
    1. Extract categories from cart
    2. Compare with bundle definitions
    3. Return highest applicable discount
    """

    cart_categories = {product.category for product in cart}

    applicable_discount = 0

    for bundle, discount in bundle_discounts.items():

        if bundle.issubset(cart_categories):
            applicable_discount = max(applicable_discount, discount)

    return applicable_discount


# --------------------------------------------------
# Test Bundle Discount
# --------------------------------------------------

discount = check_bundle_discount(customer_cart)

print("Cart Categories:", {p.category for p in customer_cart})
print("Applicable Discount:", discount, "%")


# --------------------------------------------------
# 4️⃣ Performance Benchmark
# --------------------------------------------------

"""
We compare creation time of set vs frozenset.
timeit runs the operation many times to measure average speed.
"""

set_time = timeit.timeit(
    "set(['Electronics','Books'])",
    number=100000
)

frozenset_time = timeit.timeit(
    "frozenset(['Electronics','Books'])",
    number=100000
)

print("\nPerformance Benchmark (100000 iterations)")
print("Set Creation Time:", set_time)
print("Frozenset Creation Time:", frozenset_time)


"""
Observation:

• set creation is usually slightly faster
• frozenset creation is slightly slower due to immutability and hashing

However the difference is very small and usually negligible.

Example Results:

Set creation time:       ~0.015 seconds
Frozenset creation time: ~0.018 seconds

Conclusion:

Use set when you need mutability.
Use frozenset when you need:

• dictionary keys
• stable combinations
• safe immutable collections
"""