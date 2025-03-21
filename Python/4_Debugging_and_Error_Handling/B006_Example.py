import json


def process_order(order_data):
    """
    ❌ Directly assuming the input is always a valid JSON string without validating it.
    It's better to validate if the input is a valid JSON string to avoid potential failures when the data is invalid.
    """
    try:
        order = json.loads(order_data)  # Might fail if data is invalid.

        """
        ❌ Logging is recommended instead of using print statements for better traceability and debugging.
        Print statements should be replaced with structured logging to improve visibility in production environments.
        """
        print("Processing order:", order["order_id"])

        """
        ❌ Potential division by zero (order["quantity"] could be zero).
        Before performing calculations, check for zero or negative values.
        """
        if order["quantity"] == 0:
            print("Error: Quantity cannot be zero.")
            return  # Early return to avoid division by zero error.

        """
        ❌ It's better to validate the presence of required keys before accessing them.
        This avoids the risk of a KeyError if the keys are missing from the input data.
        """
        if "total_price" not in order or "quantity" not in order:
            print("Error: Missing required order details.")
            return  # Early exit if keys are missing.

        price_per_item = order["total_price"] / order["quantity"]

        """
        ❌ Using print statements for status updates.
        Structured logging should be used instead of print statements for better traceability.
        """
        print("Order processed successfully!")  # No structured logging.

    except json.JSONDecodeError as e:
        """
        ❌ Catching general exceptions might make debugging difficult.
        It's better to catch specific errors (e.g., missing keys) to make debugging easier.
        """
        print("Error: Invalid JSON data. Please check the input format.")

    except ZeroDivisionError as e:
        """
        ❌ Providing detailed error messages is better than a generic "Something went wrong!" message.
        It's important to provide meaningful error messages with relevant context to help troubleshoot issues.
        """
        print("Error: Division by zero. Quantity must be greater than zero.")

    except KeyError as e:
        """
        ❌ Catching general exceptions might make debugging difficult.
        It's better to catch specific errors (e.g., missing keys) to make debugging easier.
        """
        print(f"Error: Missing required field {str(e)}.")

    except Exception as e:
        """
        ❌ Providing detailed error messages is better than a generic "Something went wrong!" message.
        It's important to provide meaningful error messages with relevant context to help troubleshoot issues.
        """
        print(f"Something went wrong: {e}")  # More detailed error message.


# Simulating an invalid order input
process_order(
    '{"order_id": 123, "total_price": 100, "quantity": 0}'
)  # Edge case with quantity 0.
