def process_customer(customer_data):
    """
    ❌ Missing key checks are handled with print statements.
    Instead of printing errors to the console, it's better to log them or raise exceptions.
    """
    if "name" not in customer_data:
        print("Error: Missing customer name.")
        return  # Early exit if "name" is not found, preventing errors.
    
    if "age" not in customer_data:
        print("Error: Missing customer age.")
        return  # Early exit if "age" is not found, preventing errors.
    
    """
    ❌ The input validation for age only checks if it can be converted to an integer.
    No check for the range or reasonable values of the age.
    """
    try:
        age = int(customer_data["age"])  # Assumes "age" is always a valid integer.
    except ValueError:  # ❌ Fails to handle all edge cases of invalid input.
        print("Error: Invalid age value. Age must be an integer.")
        return  # Return early if the conversion fails to prevent the crash.
    
    print("Processing customer:", customer_data["name"])
    print("Customer age:", age)

# Testing with missing key and invalid age (No error handling)
process_customer(
    {"age": "twenty"}  # ❌ Will crash due to missing "name" and invalid "age".
)  

process_customer(
    {"name": "Alice", "age": "twenty"}  # ❌ Will crash due to invalid integer conversion.
)
