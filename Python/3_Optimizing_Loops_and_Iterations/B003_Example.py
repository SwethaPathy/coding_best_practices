"""An e-commerce platform applies discount coupons to matching customer orders.
The company has 1 million orders and 100,000 discount coupons.
"""

import time
import random

# Simulating 1 million customer orders (order_id, customer_id, amount)
orders = [
    (f"ORD{num}", f"CUST{random.randint(1, 500_000)}", random.randint(20, 500))
    for num in range(1, 1_000_001)
]

# Simulating 100,000 discount coupons (customer_id, discount_percent)
discounts = {
    f"CUST{random.randint(1, 500_000)}": random.randint(5, 30) for _ in range(100_000)
}


# ❌ Inefficient Filtering: Nested loops result in an O(n * m) complexity (1M * 100K operations)
def apply_discounts(orders, discounts):
    discounted_orders = []

    for order in orders:  # ❌ O(n) loop (1M iterations)
        matched_discounts = [
            discounts[cust_id] for cust_id in discounts if cust_id == order[1]
        ]  # ❌ O(m) lookup (100K iterations) → Inefficient and unnecessary loop.

        if matched_discounts:  # ✅ Uses a list, but checking dictionary keys is better.
            discounted_orders.append(
                (order[0], order[1], order[2], matched_discounts[0])
            )

    return discounted_orders


start_time = time.time()
discounted_orders = apply_discounts(orders, discounts)
end_time = time.time()

# ❌ Poor Performance: Takes too long due to inefficient loops.
print(f"Execution Time (Bad Code): {end_time - start_time:.2f} seconds")
print(f"Discounted Orders Found: {len(discounted_orders)}")
