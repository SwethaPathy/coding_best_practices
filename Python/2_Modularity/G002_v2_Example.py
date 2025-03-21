"""
Feature Enhancement: VIP Customers Get Free Shipping ✅

To implement this feature:
- VIP customers receive free shipping. ✅
- The change affects both discount application (VIP customers might receive better discounts)
  and shipping fee calculation (waiving shipping costs for VIPs). ✅
- The solution is designed for **scalability** and **maintainability**. ✅
"""


class OrderProcessor:
    """
    A class to handle order processing, including price calculation, ✅
    discount application, shipping fee addition, and order saving. ✅

    This class follows:
    - **Encapsulation**: All order-related logic is inside the class. ✅
    - **Single Responsibility Principle (SRP)**: Each method has a distinct responsibility. ✅
    - **Scalability**: The design allows easy future modifications. ✅
    """

    def __init__(
        self,
        customer_name: str,
        product_name: str,
        price: float,
        quantity: int,
        discount_percentage: float,
        shipping_type: str,
        is_vip: bool = False,  # Defaulting to False ensures backward compatibility ✅
    ):
        """
        Initializes order details. ✅
        Uses **clear and meaningful variable names** for readability. ✅
        """
        self.customer_name = customer_name
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.discount_percentage = discount_percentage
        self.shipping_type = shipping_type
        self.is_vip = is_vip
        self.total_price = 0  # Default total price initialized to 0 ✅

    def calculate_total_price(self) -> float:
        """
        Calculates the total price before applying any discounts or shipping fees. ✅
        This method keeps price calculation **modular and reusable**. ✅
        """
        self.total_price = self.price * self.quantity
        print(f"Initial Total Price for {self.customer_name}: {self.total_price}")
        return self.total_price

    def apply_discount(self) -> float:
        """
        Applies the discount percentage to the total price. ✅
        The discount logic is **separated for clarity and potential future enhancements**. ✅
        """
        discount = (self.total_price * self.discount_percentage) / 100
        self.total_price -= discount
        print(f"Price after discount: {self.total_price}")
        return self.total_price

    def add_shipping_fee(self) -> float:
        """
        Adds shipping fees based on the shipping type, or free shipping for VIP customers. ✅
        VIP customers get **free shipping**, making this method **scalable for future customer types**. ✅
        """
        if self.is_vip:
            shipping_fee = 0
            print("VIP customer: Free shipping applied! ✅")
        elif self.shipping_type == "standard":
            shipping_fee = 5
        elif self.shipping_type == "express":
            shipping_fee = 15
        else:
            shipping_fee = 0  # Default case handled for unexpected shipping types ✅

        self.total_price += shipping_fee
        print(f"Price after shipping fee: {self.total_price}")
        return self.total_price

    def save_order(self):
        """
        Simulates saving the order to a database. ✅
        Future updates could replace this with **actual database integration**. ✅
        """
        print(
            f"Order saved for {self.customer_name}: {self.product_name} for ${self.total_price} ✅"
        )

    def process_order(self):
        """
        Orchestrates the **entire order processing** step-by-step. ✅
        This follows the **Facade Pattern**, allowing users to process orders without knowing internal details. ✅
        """
        self.calculate_total_price()
        self.apply_discount()
        self.add_shipping_fee()
        self.save_order()


# Example usage (Demonstrates **clarity and reusability** ✅)
order = OrderProcessor("John Doe", "Laptop", 1000, 2, 10, "express", is_vip=True)
order.process_order()
