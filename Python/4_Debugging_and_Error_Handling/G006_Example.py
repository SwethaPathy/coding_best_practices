import json
import logging

# Best practice: Configure logging for better traceability, including log levels, file rotation, and a consistent format.
logging.basicConfig(
    filename="order_processing.log",  # Logs will be saved to a file for long-term storage and troubleshooting.
    level=logging.DEBUG,  # DEBUG level ensures all log messages are captured.
    format="%(asctime)s - %(levelname)s - %(message)s",  # Includes timestamp and log level for easier reading.
)


class OrderProcessingError(Exception):
    """Custom exception for order processing errors"""

    pass


def process_order(order_data):
    try:
        # Best practice: Validate and parse order data
        order = json.loads(order_data)
        logging.info(f"Processing order: {order.get('order_id')}")

        # Best practice: Handle potential division by zero error and raise a custom exception for business logic errors.
        if order["quantity"] == 0:
            raise OrderProcessingError("Quantity cannot be zero.")  # Custom exception is used appropriately for business logic validation.

        price_per_item = order["total_price"] / order["quantity"]

        logging.info(f"Order {order.get('order_id')} processed successfully.")
        return price_per_item

    # Best practice: Catch specific exceptions first and then general exceptions to provide more meaningful error handling.
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON data: {e}")
    except ZeroDivisionError as e:
        # Best practice: Handle specific errors like division by zero. This can happen if `quantity` is zero.
        logging.error(f"Math error in order processing: {e}")
    except OrderProcessingError as e:
        # Best practice: Use custom exceptions for business logic validation and log warnings accordingly.
        logging.warning(f"Order Processing Warning: {e}")
    except Exception as e:
        # Best practice: Catch any unexpected errors and log the full stack trace for debugging.
        logging.exception(f"Unexpected error occurred!:{e}")  # Logs the complete stack trace for better diagnosis.


# Simulating an invalid order input
process_order('{"order_id": 123, "total_price": 100, "quantity": 0}')  # This will trigger a custom exception (quantity == 0)
