"""
Feature Enhancement: VIP Customers Get Free Shipping ❌

To implement this feature:
- VIP customers receive free shipping.
- The change affects both discount application (VIP customers might receive better discounts)
  and shipping fee calculation (waiving shipping costs for VIPs).
"""


def process_order(
    customer_name,
    product_name,
    price,
    quantity,
    discount_percentage,
    shipping_type,
    is_vip=False,
):
    # ❌ Lacks proper input validation (e.g., negative price or quantity)
    # Step 1: Calculate total price
    total_price = (
        price * quantity
    )  # ❌ Direct calculations inline, making debugging harder
    print(
        f"Total Price for {customer_name}: {total_price}"
    )  # ❌ Uses print instead of logging

    # Step 2: Apply discount
    total_price -= total_price * discount_percentage / 100
    print(
        f"Price after discount: {total_price}"
    )  # ❌ Doesn't check if discount percentage is valid (e.g., >100%)

    # Step 3: Determine shipping fee
    # ❌ Hardcoded logic without flexibility (future expansion might be difficult)
    if is_vip:
        shipping_fee = 0
        print("VIP customer: Free shipping applied!")  # ❌ Not using structured logging
    elif shipping_type == "standard":
        shipping_fee = 5
    elif shipping_type == "express":
        shipping_fee = 15
    else:
        shipping_fee = 0  # ❌ Doesn't handle unknown shipping types properly (e.g., should raise an error)

    total_price += shipping_fee
    print(
        f"Price after shipping fee: {total_price}"
    )  # ❌ No clear separation between business logic and output

    # Step 4: Save the order
    print(
        f"Order saved for {customer_name}: {product_name} for ${total_price}"
    )  # ❌ Order persistence should be handled by a dedicated function or database


# ❌ Example usage should be inside a `main` function or protected under `if __name__ == "__main__":`
process_order("John Doe", "Laptop", 1000, 2, 10, "express", is_vip=True)
