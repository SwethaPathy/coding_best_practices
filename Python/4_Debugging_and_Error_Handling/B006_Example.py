import json


def process_order(order_data):
    try:
        # Best practice: Validate if order_data is a valid JSON string.
        # Missed best practice: Directly assuming the input is always a valid JSON string without validating it.
        order = json.loads(order_data)  # Might fail if data is invalid.
        
        # Best practice: Use structured logging instead of simple print statements.
        # Missed best practice: Logging is recommended instead of using print statements for better traceability and debugging.
        print("Processing order:", order["order_id"])

        # Best practice: Check for zero or negative values before performing calculations.
        # Missed best practice: Potential division by zero (order["quantity"] could be zero).
        if order["quantity"] == 0:
            print("Error: Quantity cannot be zero.")
            return  # Early return to avoid division by zero error.

        # Best practice: Validate presence of required keys in the input data to avoid KeyError.
        if "total_price" not in order or "quantity" not in order:
            print("Error: Missing required order details.")
            return  # Early exit if keys are missing.
        
        # Simulating a division error if quantity is 0
        price_per_item = order["total_price"] / order["quantity"]

        # Best practice: Structured logging and providing more informative messages would be better.
        print("Order processed successfully!")  # No structured logging.
    
    except json.JSONDecodeError as e:  # Specific exception for invalid JSON input.
        # Best practice: Catching specific exceptions (JSONDecodeError in this case) allows for better error handling.
        print("Error: Invalid JSON data. Please check the input format.")
    
    except ZeroDivisionError as e:  # Handling specific exception for division by zero.
        # Best practice: Handle known errors like division by zero.
        print("Error: Division by zero. Quantity must be greater than zero.")
    
    except KeyError as e:  # Specific exception handling for missing keys.
        # Missed best practice: Catching general exceptions might make debugging difficult. It's better to handle specific errors.
        print(f"Error: Missing required field {str(e)}.")
    
    except Exception as e:  # Catches everything, making debugging hard.
        # Missed best practice: Providing detailed error messages is better than a generic "Something went wrong!" message.
        print(f"Something went wrong: {e}")  # More detailed error message.
        

# Simulating an invalid order input
process_order('{"order_id": 123, "total_price": 100, "quantity": 0}')  # Edge case with quantity 0.
