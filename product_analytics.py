"""
Product Analytics Tool
Analyzes shopping behavior using tuples and sets.
"""

from collections import namedtuple

# --------------------------------------------------
# 1️⃣ Define Named Tuple
# --------------------------------------------------

Product = namedtuple("Product", ["id", "name", "category", "price"])


# --------------------------------------------------
# 2️⃣ Product Catalog (15 products across 4 categories)
# --------------------------------------------------

catalog = {

    # Electronics
    Product(1, "Laptop", "Electronics", 75000),
    Product(2, "Smartphone", "Electronics", 50000),
    Product(3, "Headphones", "Electronics", 3000),
    Product(4, "Smartwatch", "Electronics", 10000),

    # Clothing
    Product(5, "T-Shirt", "Clothing", 800),
    Product(6, "Jeans", "Clothing", 2000),
    Product(7, "Jacket", "Clothing", 3500),
    Product(8, "Sneakers", "Clothing", 4000),

    # Books
    Product(9, "Clean Code", "Books", 500),
    Product(10, "Python Crash Course", "Books", 700),
    Product(11, "Atomic Habits", "Books", 450),
    Product(12, "Deep Learning", "Books", 900),

    # Home
    Product(13, "Coffee Maker", "Home", 2500),
    Product(14, "Desk Lamp", "Home", 1200),
    Product(15, "Office Chair", "Home", 7000)
}


# Convert catalog to list for easier indexing
catalog_list = list(catalog)


# --------------------------------------------------
# 3️⃣ Customer Cart Sets
# --------------------------------------------------

customer_1_cart = {catalog_list[0], catalog_list[2], catalog_list[8], catalog_list[13]}
customer_2_cart = {catalog_list[1], catalog_list[2], catalog_list[8], catalog_list[9]}
customer_3_cart = {catalog_list[0], catalog_list[3], catalog_list[8], catalog_list[10]}
customer_4_cart = {catalog_list[0], catalog_list[2], catalog_list[8], catalog_list[14]}
customer_5_cart = {catalog_list[0], catalog_list[2], catalog_list[8], catalog_list[12]}

all_carts = [
    customer_1_cart,
    customer_2_cart,
    customer_3_cart,
    customer_4_cart,
    customer_5_cart
]


# --------------------------------------------------
# 4️⃣ Analyze Shopping Behaviour
# --------------------------------------------------

def bestsellers(carts):
    """Products appearing in ALL carts"""
    return set.intersection(*carts)


def catalog_reach(carts):
    """Products appearing in ANY cart"""
    return set.union(*carts)


def exclusive_purchases(customer_cart, other_carts):
    """Products bought only by one customer"""
    others_union = set.union(*other_carts)
    return customer_cart - others_union


# --------------------------------------------------
# 5️⃣ Product Recommendation
# --------------------------------------------------

def recommend_products(customer_cart, carts):
    """
    Suggest products other customers bought
    but this customer didn't.
    """

    others = [cart for cart in carts if cart != customer_cart]

    other_products = set.union(*others)

    recommendations = other_products - customer_cart

    return recommendations


# --------------------------------------------------
# 6️⃣ Category Summary
# --------------------------------------------------

def category_summary():
    """
    Returns mapping of categories to product names
    """

    categories = {product.category for product in catalog}

    summary = {
        category: {p.name for p in catalog if p.category == category}
        for category in categories
    }

    return summary


# --------------------------------------------------
# Demo Execution
# --------------------------------------------------

if __name__ == "__main__":

    print("\n--- Bestsellers (Products in ALL carts) ---")
    print({p.name for p in bestsellers(all_carts)})

    print("\n--- Catalog Reach (Products in ANY cart) ---")
    print({p.name for p in catalog_reach(all_carts)})

    print("\n--- Exclusive Purchases (Customer 1) ---")
    print({p.name for p in exclusive_purchases(customer_1_cart, all_carts[1:])})

    print("\n--- Recommendations for Customer 1 ---")
    print({p.name for p in recommend_products(customer_1_cart, all_carts)})

    print("\n--- Category Summary ---")
    print(category_summary())