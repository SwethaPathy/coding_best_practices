def process_customer(customer_data):
    # Best practice: Use .get() to safely access dictionary keys and provide a default value if the key is missing.
    # In this case, defaulting "name" to "Unknown Customer" if the key is missing.
    name = customer_data.get("name", "Unknown Customer")  # Provides a default value for missing "name"

    # It checks if "age" is a string and whether it contains only digits, but this doesn't handle cases where the "age" 
    # is a valid number (e.g., "25" as a string is valid but not converted).
    # Check if 'age' exists and is a valid number, else set to default
    age = customer_data.get("age", "N/A")  # Default to "N/A" if "age" is missing
    
    if isinstance(age, str) and not age.isdigit():  # This checks if age is a non-digit string but doesn't handle numbers properly.
        age = "Invalid Age"  # Provide a meaningful default value when age is invalid

    # Best practice: Ensure that meaningful logs or prints are provided when data is processed.
    print(f"Processing customer: {name}")
    print(f"Customer age: {age}")


# Testing with missing key and invalid age
process_customer({"age": "twenty"})  # No errors, provides defaults (invalid age handled as "Invalid Age")
process_customer({"name": "Alice", "age": "twenty"})  # No errors, validates "age" as invalid
process_customer({"name": "Bob", "age": "25"})  # Works correctly
