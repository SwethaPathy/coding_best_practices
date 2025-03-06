import time


def process_numbers(numbers):
    squared_numbers = []
    for num in numbers:
        squared_numbers.append(num * num)

    even_squared_numbers = []
    for num in squared_numbers:
        if num % 2 == 0:
            even_squared_numbers.append(num)

    total_sum = 0
    for num in even_squared_numbers:
        total_sum += num

    return total_sum


# Timing the execution of the bad code
start_time = time.time()

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_bad = process_numbers(numbers)

end_time = time.time()
execution_time_bad = end_time - start_time
print(f"Bad Code Execution Time: {execution_time_bad:.6f} seconds")
print(f"Result: {result_bad}")
