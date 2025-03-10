def process_customer(customer_data):
    # Check if 'name' key exists, else set default
    name = customer_data.get("name", "Unknown Customer")

    # Check if 'age' exists and is a valid number, else set to default
    age = customer_data.get("age", "N/A")
    if isinstance(age, str) and not age.isdigit():
        age = "Invalid Age"  # Provide a meaningful default value

    print(f"Processing customer: {name}")
    print(f"Customer age: {age}")


# Testing with missing key and invalid age
process_customer({"age": "twenty"})  # No errors, provides defaults
process_customer({"name": "Alice", "age": "twenty"})  # No errors, validates "age"
process_customer({"name": "Bob", "age": "25"})  # Works correctly
