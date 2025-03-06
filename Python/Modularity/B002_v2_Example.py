"""Let's say you need to add a new feature: "VIP customers get free shipping".

To implement this feature:

We’ll check if the customer is a VIP and if so, waive the shipping fees.
The change needs to be made in both the discount application (to check if the customer is VIP) and the shipping fee calculation (to waive the shipping fee for VIP customers)."""


def process_order(customer_name,
                  product_name,
                  price,
                  quantity,
                  discount_percentage,
                  shipping_type,
                  is_vip=False):
  # Step 1: Calculate total price
  total_price = price * quantity
  print(f"Total Price for {customer_name}: {total_price}")

  # Step 2: Apply discount
  total_price -= (total_price * discount_percentage / 100)
  print(f"Price after discount: {total_price}")

  # Step 3: Add shipping fee or free shipping for VIP
  if is_vip:
    shipping_fee = 0
    print("VIP customer: Free shipping applied!")
  elif shipping_type == "standard":
    shipping_fee = 5
  elif shipping_type == "express":
    shipping_fee = 15
  else:
    shipping_fee = 0
  total_price += shipping_fee
  print(f"Price after shipping fee: {total_price}")

  # Step 4: Save the order
  print(f"Order saved for {customer_name}: {product_name} for ${total_price}")


# Example usage
process_order("John Doe", "Laptop", 1000, 2, 10, "express", is_vip=True)
