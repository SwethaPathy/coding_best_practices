def process_customer(customer_data):
    print("Processing customer:", customer_data["name"])  # Assumes "name" always exists
    age = int(customer_data["age"])  # Assumes "age" is always a valid integer
    print("Customer age:", age)


# Testing with missing key and invalid age (No error handling)
process_customer(
    {"age": "twenty"}
)  # Will crash due to missing "name" and invalid "age"
process_customer(
    {"name": "Alice", "age": "twenty"}
)  # Will crash due to invalid integer conversion
