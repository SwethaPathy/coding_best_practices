"""In an e-commerce application, we need to process customer orders, calculate the total price, apply discounts, and manage customer information. Over time, we want to scale the application and handle different types of products, shipping methods, and promotions."""


def process_order(customer_name, product_name, price, quantity,
                  discount_percentage, shipping_type):
  # Calculate total price
  total_price = price * quantity
  print(f"Total Price for {customer_name}: {total_price}")

  # Apply discount
  total_price -= (total_price * discount_percentage / 100)
  print(f"Price after discount: {total_price}")

  # Add shipping fee
  if shipping_type == "standard":
    shipping_fee = 5
  elif shipping_type == "express":
    shipping_fee = 15
  else:
    shipping_fee = 0
  total_price += shipping_fee
  print(f"Price after shipping fee: {total_price}")

  # Print final total price
  print(f"Final Price: {total_price}")

  # Save customer order
  save_order(customer_name, product_name, total_price)


def save_order(customer_name, product_name, total_price):
  print(
      f"Order saved: {customer_name} ordered {product_name} for ${total_price}"
  )


# Example usage
process_order("John Doe", "Laptop", 1000, 2, 10, "express")
