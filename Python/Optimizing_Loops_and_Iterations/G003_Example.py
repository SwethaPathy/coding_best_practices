"""An e-commerce platform applies discount coupons to matching customer orders. The company has 1 million orders and 100,000 discount coupons."""

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


# GOOD: Uses dictionary lookup for O(n) performance
def apply_discounts(orders, discounts):
    return [
        (order[0], order[1], order[2], discounts[order[1]])
        for order in orders
        if order[1] in discounts
    ]  # O(n) instead of O(n*m)


start_time = time.time()
discounted_orders = apply_discounts(orders, discounts)
end_time = time.time()

print(f"Execution Time (Good Code): {end_time - start_time:.2f} seconds")
print(f"Discounted Orders Found: {len(discounted_orders)}")
