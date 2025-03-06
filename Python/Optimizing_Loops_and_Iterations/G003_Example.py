import time


def process_numbers_optimized(numbers):
    # Using list comprehension to square and filter in one go
    squared_even_numbers = [
        num * num for num in numbers if (num * num) % 2 == 0
    ]

    # Use sum() to directly calculate the sum of the numbers
    return sum(squared_even_numbers)


# Alternative version using map() and filter()
def process_numbers_optimized_map_filter(numbers):
    # Using map() to square the numbers, and filter() to keep only even squares
    squared_numbers = map(lambda x: x * x, numbers)
    even_squared_numbers = filter(lambda x: x % 2 == 0, squared_numbers)

    # Use sum() to directly calculate the sum of the numbers
    return sum(even_squared_numbers)


# Timing the execution of the good code
start_time = time.time()

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_good = process_numbers_optimized(numbers)

end_time = time.time()
execution_time_good = end_time - start_time
print(f"Good Code Execution Time: {execution_time_good:.6f} seconds")
print(f"Result: {result_good}")
