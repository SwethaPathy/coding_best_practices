"""In an e-commerce application, we need to process customer orders, calculate the total price, apply discounts, and manage customer information. Over time, we want to scale the application and handle different types of products, shipping methods, and promotions."""


class OrderProcessor:

  def __init__(self, customer_name, product_name, price, quantity,
               discount_percentage, shipping_type):
    self.customer_name = customer_name
    self.product_name = product_name
    self.price = price
    self.quantity = quantity
    self.discount_percentage = discount_percentage
    self.shipping_type = shipping_type
    self.total_price = 0

  def calculate_total_price(self):
    """
      Calculates the total price before any discounts or shipping fees.
      """
    self.total_price = self.price * self.quantity
    print(f"Initial Total Price for {self.customer_name}: {self.total_price}")
    return self.total_price

  def apply_discount(self):
    """
      Applies the discount to the total price.
      """
    discount = (self.total_price * self.discount_percentage) / 100
    self.total_price -= discount
    print(f"Price after discount: {self.total_price}")
    return self.total_price

  def add_shipping_fee(self):
    """
      Adds shipping fees based on the shipping type.
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
      Saves the order.
      """
    print(
        f"Order saved: {self.customer_name} ordered {self.product_name} for ${self.total_price}"
    )

  def process_order(self):
    """
      Orchestrates the entire order processing.
      """
    self.calculate_total_price()
    self.apply_discount()
    self.add_shipping_fee()
    self.save_order()


# Example usage
order = OrderProcessor("John Doe", "Laptop", 1000, 2, 10, "express")
order.process_order()
