import json
import logging

# ✅ Configure logging for better traceability, including log levels, file rotation, and a consistent format.
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
        # ✅ Validate and parse order data
        order = json.loads(order_data)
        logging.info(f"Processing order: {order.get('order_id')}")

        # ✅ Handle potential division by zero error and raise a custom exception for business logic errors.
        if order["quantity"] == 0:
            raise OrderProcessingError("Quantity cannot be zero.")  # Custom exception is used appropriately for business logic validation.

        price_per_item = order["total_price"] / order["quantity"]

        # ✅ Structured logging for successful processing.
        logging.info(f"Order {order.get('order_id')} processed successfully.")
        return price_per_item

    except json.JSONDecodeError as e:
        # ✅ Handle JSON decode error, which may happen if input is not valid JSON.
        logging.error(f"Invalid JSON data: {e}")
    except ZeroDivisionError as e:
        # ✅ Handle division by zero errors, which may happen if `quantity` is zero.
        logging.error(f"Math error in order processing: {e}")
    except OrderProcessingError as e:
        # ✅ Handle the custom business logic error for zero quantity.
        logging.warning(f"Order Processing Warning: {e}")
    except Exception as e:
        # ✅ Catch any unexpected errors and log the full stack trace for debugging.
        logging.exception(f"Unexpected error occurred!:{e}")  # Logs the complete stack trace for better diagnosis.


# Simulating an invalid order input
process_order('{"order_id": 123, "total_price": 100, "quantity": 0}')  # This will trigger a custom exception (quantity == 0)
