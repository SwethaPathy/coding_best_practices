import time
import random
import threading

# Simulating 1 million orders (order_id, customer_id, amount)
orders = [[f"ORD{num}", f"CUST{random.randint(1, 500_000)}", random.randint(20, 500)] for num in range(1, 1_000_001)]

# Simulating 100,000 discount coupons stored in a Linked List (Inefficient)
class Node:
    def __init__(self, customer_id, discount):
        self.customer_id = customer_id
        self.discount = discount
        self.next = None

class LinkedListDiscounts:
    def __init__(self):
        self.head = None

    def add_discount(self, customer_id, discount):
        new_node = Node(customer_id, discount)
        new_node.next = self.head
        self.head = new_node

    def get_discount(self, customer_id):
        current = self.head
        while current:  # Inefficient O(n) lookup
            if current.customer_id == customer_id:
                return current.discount
            current = current.next
        return 0

# Creating a Linked List for discounts (BAD: Slow for lookups)
discounts = LinkedListDiscounts()
for _ in range(100_000):
    discounts.add_discount(f"CUST{random.randint(1, 500_000)}", random.randint(5, 30))

# BAD: Uses a slow single-threaded approach
def process_orders():
    discounted_orders = []
    for order in orders:
        discount = discounts.get_discount(order[1])  # O(n) lookup for each order
        discounted_orders.append((order[0], order[1], order[2], discount))
    return discounted_orders

start_time = time.time()
discounted_orders = process_orders()
end_time = time.time()

print(f"Execution Time (Bad Code): {end_time - start_time:.2f} minutes")
print(f"Discounted Orders Processed: {len(discounted_orders)}")
