"""
Problem Statement:
In an e-commerce application, we need to process customer orders,
calculate the total price, apply discounts, and manage customer information.
Over time, we want to scale the application and handle different types of products,
shipping methods, and promotions.
"""


class OrderProcessor:
    """
    ✅ Follows Object-Oriented Programming (OOP) principles by encapsulating order processing logic into a class.
    ✅ Adheres to the Single Responsibility Principle (SRP) - Each method handles a distinct task.
    """

    def __init__(
        self,
        customer_name,
        product_name,
        price,
        quantity,
        discount_percentage,
        shipping_type,
    ):
        """
        ✅ Uses meaningful variable names (e.g., `customer_name`, `product_name`).
        ✅ Organizes instance variables within a constructor for better readability and structure.
        """
        self.customer_name = customer_name
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.discount_percentage = discount_percentage
        self.shipping_type = shipping_type
        self.total_price = 0  # ✅ Initializes total price to avoid undefined variables.

    def calculate_total_price(self):
        """
        ✅ Follows the Single Responsibility Principle (SRP) - Only calculates total price.
        """
        self.total_price = self.price * self.quantity
        print(f"Initial Total Price for {self.customer_name}: {self.total_price}")
        return self.total_price

    def apply_discount(self):
        """
        ✅ Separates discount logic into its own method for maintainability.
        ✅ Ensures discounts are applied in a modular way for easy future enhancements.
        """
        discount = (self.total_price * self.discount_percentage) / 100
        self.total_price -= discount
        print(f"Price after discount: {self.total_price}")
        return self.total_price

    def add_shipping_fee(self):
        """
        ✅ Uses a structured approach to adding shipping fees.
        ✅ Avoids hardcoding values within the main logic.
        """
        shipping_fee = 0
        if self.shipping_type == "standard":
            shipping_fee = 5
        elif self.shipping_type == "express":
            shipping_fee = 15

        self.total_price += shipping_fee
        print(f"Price after shipping fee: {self.total_price}")
        return self.total_price

    def save_order(self):
        """
        ✅ Isolates the order-saving logic for better maintainability.
        ✅ Can later be expanded to integrate with a database or an API.
        """
        print(
            f"Order saved: {self.customer_name} ordered {self.product_name} for ${self.total_price}"
        )

    def process_order(self):
        """
        ✅ Orchestrates the entire order processing workflow, ensuring clear code organization.
        ✅ Ensures that each step is modular and easy to modify.
        """
        self.calculate_total_price()
        self.apply_discount()
        self.add_shipping_fee()
        self.save_order()


# Example usage
order = OrderProcessor("John Doe", "Laptop", 1000, 2, 10, "express")
order.process_order()
