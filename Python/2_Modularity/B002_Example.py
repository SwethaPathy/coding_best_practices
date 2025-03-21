"""
Problem Statement:
    In an e-commerce application, we need to process customer orders,
    calculate the total price, apply discounts, and manage customer information.
    Over time, we want to scale the application and handle different types of products,
    shipping methods, and promotions.
"""


def process_order(
    customer_name, product_name, price, quantity, discount_percentage, shipping_type
):
    # ❌ Violates Single Responsibility Principle (SRP) - This function does multiple things:
    #    1. Calculates total price
    #    2. Applies discount
    #    3. Determines shipping fee
    #    4. Prints details
    #    5. Saves the order
    #    This makes it harder to maintain and scale.

    # Calculate total price
    total_price = price * quantity
    print(
        f"Total Price for {customer_name}: {total_price}"
    )  # ❌ Uses print() instead of proper logging

    # Apply discount
    total_price -= total_price * discount_percentage / 100
    print(
        f"Price after discount: {total_price}"
    )  # ❌ Again, uses print() instead of logging

    # Determine shipping fee (❌ Poor extensibility - Adding new shipping types requires modifying this function)
    if shipping_type == "standard":
        shipping_fee = 5
    elif shipping_type == "express":
        shipping_fee = 15
    else:
        shipping_fee = 0  # ❌ No validation for incorrect shipping types
    total_price += shipping_fee
    print(f"Price after shipping fee: {total_price}")

    # Print final total price
    print(f"Final Price: {total_price}")

    # Save customer order
    save_order(
        customer_name, product_name, total_price
    )  # ❌ Directly calling another function with minimal separation of concerns


def save_order(customer_name, product_name, total_price):
    # ❌ Lacks error handling - What if saving to a database fails?
    print(
        f"Order saved: {customer_name} ordered {product_name} for ${total_price}"
    )  # ❌ Uses print() instead of logging


# Example usage
process_order("John Doe", "Laptop", 1000, 2, 10, "express")
