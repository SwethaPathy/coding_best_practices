"""Let's say you need to add a new feature: "VIP customers get free shipping".

To implement this feature:

We’ll check if the customer is a VIP and if so, waive the shipping fees.
The change needs to be made in both the discount application (to check if the customer is VIP) and the shipping fee calculation (to waive the shipping fee for VIP customers)."""


class OrderProcessor:

  def __init__(self,
               customer_name,
               product_name,
               price,
               quantity,
               discount_percentage,
               shipping_type,
               is_vip=False):
    self.customer_name = customer_name
    self.product_name = product_name
    self.price = price
    self.quantity = quantity
    self.discount_percentage = discount_percentage
    self.shipping_type = shipping_type
    self.is_vip = is_vip
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
      Adds shipping fees based on the shipping type, or free shipping for VIP customers.
      """
    if self.is_vip:
      shipping_fee = 0
      print("VIP customer: Free shipping applied!")
    elif self.shipping_type == "standard":
      shipping_fee = 5
    elif self.shipping_type == "express":
      shipping_fee = 15
    else:
      shipping_fee = 0

    self.total_price += shipping_fee
    print(f"Price after shipping fee: {self.total_price}")
    return self.total_price

  def save_order(self):
    """
      Simulates saving the order to the database (prints to console).
      """
    print(
        f"Order saved for {self.customer_name}: {self.product_name} for ${self.total_price}"
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
order = OrderProcessor("John Doe",
                       "Laptop",
                       1000,
                       2,
                       10,
                       "express",
                       is_vip=True)
order.process_order()
