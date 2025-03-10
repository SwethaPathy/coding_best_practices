import json
import logging

# Configure logging with appropriate levels and file rotation
logging.basicConfig(
    filename="order_processing.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class OrderProcessingError(Exception):
    """Custom exception for order processing errors"""

    pass


def process_order(order_data):
    try:
        # Validate and parse order data
        order = json.loads(order_data)
        logging.info(f"Processing order: {order.get('order_id')}")

        if order["quantity"] == 0:
            raise OrderProcessingError("Quantity cannot be zero.")  # Custom exception

        price_per_item = order["total_price"] / order["quantity"]

        logging.info(f"Order {order.get('order_id')} processed successfully.")
        return price_per_item

    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON data: {e}")
    except ZeroDivisionError as e:
        logging.error(f"Math error in order processing: {e}")
    except OrderProcessingError as e:
        logging.warning(f"Order Processing Warning: {e}")
    except Exception as e:
        logging.exception(f"Unexpected error occurred!:{e}")  # Logs full stack trace


# Simulating an invalid order input
process_order('{"order_id": 123, "total_price": 100, "quantity": 0}')
