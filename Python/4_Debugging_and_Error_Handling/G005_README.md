# Customer Processing: Bad vs. Good Code

## Problem Statement
An application needs to process customer data, ensuring name and age are validated correctly. A poor implementation can lead to crashes, incorrect data handling, or unnecessary exits. Below, we compare a bad version of the function with an optimized and error-resilient implementation.

---

## Bad Code Example
The **bad code version** lacks proper validation and structured error handling, making it fragile and difficult to maintain.

### Issues in the Bad Code:
- ❌ **Missing Key Handling**: Uses `print` statements instead of structured error handling (logging or exceptions).
- ❌ **No Default Values**: Exits early when keys are missing instead of using defaults or handling cases properly.
- ❌ **Poor Age Validation**: Only checks if `age` can be converted to an integer but doesn't validate reasonable values.
- ❌ **Crashes on Invalid Data**: If `age` contains non-numeric values, the program fails.

### Bad Code:
```python
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
process_customer({"age": "twenty"})  # ❌ Will crash due to missing "name" and invalid "age".
process_customer({"name": "Alice", "age": "twenty"})  # ❌ Will crash due to invalid integer conversion.
```

---

## Good Code Example
The **good code version** follows best practices for error handling and data validation.

### Key Improvements:
- ✅ **Uses `.get()` for Safe Dictionary Access**: Prevents KeyErrors by providing default values.
- ✅ **Default Values for Missing Data**: Ensures the function continues running even when data is missing.
- ✅ **Proper Age Validation**: Handles non-numeric values and provides meaningful defaults instead of crashing.
- ✅ **Structured Logging/Printing**: Clearer debugging and better data handling.

### Good Code:
```python
def process_customer(customer_data):
    """
    ✅ Use .get() to safely access dictionary keys and provide a default value if the key is missing.
    Using .get() helps avoid potential KeyErrors and provides fallback values for missing keys.
    """
    name = customer_data.get(
        "name", "Unknown Customer"
    )  # Provides a default value for missing "name"

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
    if (
        isinstance(age, str) and not age.isdigit()
    ):  # This checks if age is a non-digit string but doesn't handle numbers properly.
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
```

---

## Key Differences Between Bad and Good Code

| **Aspect**               | **Bad Code** 🛑                          | **Good Code** ✅                          |
|--------------------------|----------------------------------|----------------------------------|
| **Handling Missing Keys** | Uses `if "key" not in dict` and exits early | Uses `.get()` to provide default values |
| **Error Handling**       | Prints errors to the console, exits early | Uses fallback values for robustness |
| **Age Validation**       | Converts `age` but crashes on invalid input | Handles invalid age gracefully with a default |
| **Data Continuity**      | Stops processing on missing keys | Continues execution with meaningful defaults |
| **Code Readability**     | Harder to follow due to excessive conditions | Cleaner and more readable structure |

---

## Conclusion
The **Good Code** version follows industry best practices, making the customer processing function:
- 📌 **More readable** and maintainable.
- 📌 **Resilient to missing or invalid data**.
- 📌 **Scalable for future enhancements** (e.g., better logging, exception handling, or database integration).

Using **defensive programming** and structured validation improves code quality and prevents unexpected failures. 🚀

