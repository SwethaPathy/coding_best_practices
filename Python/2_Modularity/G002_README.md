# E-Commerce Order Processing: Bad vs. Good Code

## Problem Statement
In an e-commerce application, we need to process customer orders, calculate the total price, apply discounts, and manage customer information. Over time, we want to scale the application and handle different types of products, shipping methods, and promotions.

## Bad Code Example

```python
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

```
The **B002_Example.py** is a procedural approach that lacks structure, making it difficult to scale and maintain.  
### Issues in the Bad Code:
- ❌ **No Code Organization**: The function `process_order` performs multiple tasks (calculation, discounting, and saving orders) in one block.
- ❌ **Hardcoded Values**: Shipping fees are embedded directly into the logic, making changes difficult.
- ❌ **No Encapsulation**: There's no use of object-oriented principles, making code reuse and maintenance challenging.
- ❌ **Poor Naming Conventions**: Variable and function names are not self-explanatory.
- ❌ **No Error Handling or Logging**: Debugging is difficult as there is no structured way to handle issues.

---

## Good Code Example
```python
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

```
The **G002_Example.py** follows best practices for scalability and maintainability.
### Key Improvements:
- ✅ **Encapsulated in a Class**: The `OrderProcessor` class organizes related data and methods.
- ✅ **Single Responsibility Principle (SRP)**: Each method performs a single, clear task.
- ✅ **Modular Design**: Methods for price calculation, discount application, and shipping fee addition allow for easy updates.
- ✅ **Better Naming Conventions**: Function and variable names are meaningful and self-explanatory.
- ✅ **Future-Proof**: The structured design allows for adding more shipping methods, discount types, and logging without breaking the code.

---

## Key Differences Between Bad and Good Code

| **Aspect**                  | **Bad Code** 🛑                           | **Good Code** ✅                             |
|-----------------------------|---------------------------------|----------------------------------|
| **Code Structure**          | Single function doing multiple tasks | Organized into a class with separate methods |
| **Encapsulation**           | No encapsulation, making reuse difficult | Uses a class (`OrderProcessor`) to encapsulate logic |
| **Single Responsibility Principle (SRP)** | Does everything in one function | Each method has a single, clear responsibility |
| **Scalability**             | Hard to extend (e.g., adding new shipping options) | Easy to scale and modify |
| **Readability**             | Poor, difficult to understand | Clear, well-structured code |
| **Hardcoded Values**        | Shipping fees are hardcoded inside logic | Uses a dedicated method (`add_shipping_fee()`) |
| **Naming Conventions**      | Generic names (`process_order`) | Descriptive names (`calculate_total_price`, `apply_discount`) |
| **Error Handling & Logging** | No structured logging or error handling | Can be extended to include logging & exception handling |

---

## Conclusion
The **Good Code** version follows industry best practices, making the order processing system:
- 📌 **More readable**
- 📌 **Easier to maintain**
- 📌 **Scalable for future enhancements** (e.g., different discount strategies, new shipping options)
