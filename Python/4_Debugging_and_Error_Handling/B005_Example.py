def process_customer(customer_data):
    # Best practice: Check for necessary keys in the input data (e.g., "name" and "age") before using them.
    if "name" not in customer_data:
        print("Error: Missing customer name.")
        return  # Early exit if "name" is not found, preventing errors.
    
    if "age" not in customer_data:
        print("Error: Missing customer age.")
        return  # Early exit if "age" is not found, preventing errors.
    
    # Missed best practice: Always validate input data types (e.g., ensure "age" is an integer).
    # Assuming "age" always exists, but no check is done to ensure it is a valid integer.
    try:
        age = int(customer_data["age"])  # Assumes "age" is always a valid integer.
    except ValueError:  # Missed best practice: Handle potential ValueError for invalid conversion.
        print("Error: Invalid age value. Age must be an integer.")
        return  # Return early if the conversion fails to prevent the crash.
    
    print("Processing customer:", customer_data["name"])
    print("Customer age:", age)

# Testing with missing key and invalid age (No error handling)
process_customer(
    {"age": "twenty"}  # Will crash due to missing "name" and invalid "age".
)  

process_customer(
    {"name": "Alice", "age": "twenty"}  # Will crash due to invalid integer conversion.
)
