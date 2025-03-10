import json


def process_order(order_data):
    try:
        # Assume order_data is a JSON string but not validating it
        order = json.loads(order_data)  # Might fail if data is invalid
        print("Processing order:", order["order_id"])  # Using print instead of logging

        # Simulating a division error if quantity is 0
        price_per_item = order["total_price"] / order["quantity"]

        print("Order processed successfully!")  # No structured logging
    except Exception as e:  # Catches everything, making debugging hard
        print("Something went wrong!")  # No error details are logged


# Simulating an invalid order input
process_order('{"order_id": 123, "total_price": 100, "quantity": 0}')
