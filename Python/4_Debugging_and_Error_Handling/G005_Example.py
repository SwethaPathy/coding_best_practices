def process_customer(customer_data):
    """
    ✅ Use .get() to safely access dictionary keys and provide a default value if the key is missing.
    Using .get() helps avoid potential KeyErrors and provides fallback values for missing keys.
    """
    name = customer_data.get("name", "Unknown Customer")  # Provides a default value for missing "name"

    """
    ✅ Defaulting to "N/A" if "age" is missing ensures that there's always a value.
    This ensures the function continues to run smoothly, even with missing data.
    """
    age = customer_data.get("age", "N/A")  # Default to "N/A" if "age" is missing
    
    """
    The check for non-digit age assumes all ages should be integers. 
    It doesn't handle the case where age might be a valid number in string form, like "25".
    Instead, it could convert the age to an integer or check for a valid number format.
    """
    if isinstance(age, str) and not age.isdigit():  # This checks if age is a non-digit string but doesn't handle numbers properly.
        age = "Invalid Age"  # Provide a meaningful default value when age is invalid

    """
    ✅ Ensure that meaningful logs or prints are provided when data is processed.
    This allows the developer to see what's going on with the data at each step.
    """
    print(f"Processing customer: {name}")
    print(f"Customer age: {age}")


# Testing with missing key and invalid age
process_customer({"age": "twenty"})  # No errors, provides defaults (invalid age handled as "Invalid Age")
process_customer({"name": "Alice", "age": "twenty"})  # No errors, validates "age" as invalid
process_customer({"name": "Bob", "age": "25"})  # Works correctly
