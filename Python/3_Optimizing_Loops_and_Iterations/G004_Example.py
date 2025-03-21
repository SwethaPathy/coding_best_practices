"""An online retail platform needs to process customer orders, apply discounts,
and generate reports in real-time."""

import time
import random
from concurrent.futures import ThreadPoolExecutor

# Simulating 1 million orders (order_id, customer_id, amount)
orders = [
    (f"ORD{num}", f"CUST{random.randint(1, 500_000)}", random.randint(20, 500))
    for num in range(1, 1_000_001)
]

# ✅ Using a HashMap (Dictionary) for fast key-based lookups
# This allows O(1) lookup time for retrieving discount information efficiently

discounts = {
    f"CUST{random.randint(1, 500_000)}": random.randint(5, 30) for _ in range(100_000)
}


# ✅ Optimized function using HashMap (O(1) lookups) and concurrency
def process_chunk(start, end):
    return [
        (
            order[0],
            order[1],
            order[2],
            discounts.get(order[1], 0),
        )  # ✅ Fast O(1) dictionary lookup
        for order in orders[start:end]
    ]


# ✅ Using ThreadPoolExecutor for parallel processing
# This ensures multi-threaded execution, improving performance on large datasets
def process_orders_parallel(num_threads=4):
    chunk_size = (
        len(orders) // num_threads
    )  # ✅ Splitting workload into chunks for parallel processing
    results = []

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [
            executor.submit(
                process_chunk, i * chunk_size, (i + 1) * chunk_size
            )  # ✅ Submitting tasks in parallel
            for i in range(num_threads)
        ]
        for future in futures:
            results.extend(
                future.result()
            )  # ✅ Merging results from parallel execution

    return results


start_time = time.time()
discounted_orders = process_orders_parallel()
end_time = time.time()

print(
    f"Execution Time (Good Code): {end_time - start_time:.2f} seconds"
)  # ✅ Efficient execution
print(
    f"Discounted Orders Processed: {len(discounted_orders)}"
)  # ✅ Ensuring all orders are processed correctly
