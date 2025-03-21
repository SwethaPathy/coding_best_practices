# E-Commerce Discount Processing: Bad vs. Good Code

## Problem Statement
In an e-commerce application, we need to process customer orders and apply discount coupons based on customer IDs. The system handles:
- **1 million customer orders**
- **100,000 discount coupons**

A naive approach can lead to performance bottlenecks due to inefficient discount lookups. We compare a **bad implementation** with an **optimized approach** to improve efficiency.

---

## Bad Code Example
The **bad code version** uses a nested loop approach (**O(n*m) complexity**), leading to **slow performance**.

### Issues in the Bad Code:
- ❌ **Inefficient Algorithm**: Iterates over **all orders** and checks **each discount one by one** (**O(n*m)** complexity).
- ❌ **Redundant Computation**: Uses an unnecessary list comprehension inside a loop, slowing down execution.
- ❌ **Scalability Issues**: Performance degrades significantly with large datasets.

### Bad Code Implementation:
```python
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

# BAD: Uses a slow approach with an inefficient filtering mechanism
def apply_discounts(orders, discounts):
    discounted_orders = []
    
    for order in orders:  # O(n) loop (1M iterations)
        matched_discounts = [
            discounts[cust_id] for cust_id in discounts if cust_id == order[1]
        ]  # O(m) lookup (100K iterations)

        if matched_discounts:  # If there is a matching discount
            discounted_orders.append(
                (order[0], order[1], order[2], matched_discounts[0])
            )

    return discounted_orders

start_time = time.time()
discounted_orders = apply_discounts(orders, discounts)
end_time = time.time()

print(f"Execution Time (Bad Code): {end_time - start_time:.2f} minutes")
print(f"Discounted Orders Found: {len(discounted_orders)}")
```

---

## Good Code Example
The **good code version** improves efficiency by using a **dictionary lookup (O(n))**, which drastically enhances performance.

### Key Improvements:
- ✅ **Optimized Algorithm**: Uses **dictionary lookups (O(1))** instead of looping over all discounts.
- ✅ **Eliminates Redundant Loops**: Reduces computation complexity from **O(n*m) to O(n)**.
- ✅ **Better Readability & Maintainability**: Uses a clean **list comprehension** for faster processing.
- ✅ **Scalability**: Handles large datasets efficiently.

### Good Code Implementation:
```python
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
    ]  # ✅ O(n) instead of O(n*m)

start_time = time.time()
discounted_orders = apply_discounts(orders, discounts)
end_time = time.time()

print(f"Execution Time (Good Code): {end_time - start_time:.2f} seconds")
print(f"Discounted Orders Found: {len(discounted_orders)}")
```

---

## Key Differences Between Bad and Good Code

| **Aspect**                  | **Bad Code** 🛑                           | **Good Code** ✅                             |
|-----------------------------|---------------------------------|----------------------------------|
| **Algorithm Efficiency**    | Uses nested loops (O(n*m)) | Uses dictionary lookup (O(n)) |
| **Performance**            | Slow, takes minutes to execute | Fast, executes in seconds |
| **Scalability**             | Not suitable for large datasets | Efficient for big data processing |
| **Code Readability**        | Complex and hard to understand | Clean and modular |
| **Redundant Computation**   | Loops through all discounts unnecessarily | Uses a direct lookup without iteration |
| **Maintainability**         | Difficult to update or extend | Easy to modify and scale |

---

## Conclusion
The **Good Code** version follows best practices, making the discount processing system:
- 📌 **More readable**
- 📌 **Highly scalable** for large datasets
- 📌 **Drastically faster** using efficient lookups

Using a **dictionary-based approach** improves both **performance and maintainability**, making it ideal for real-world e-commerce applications. 🚀

