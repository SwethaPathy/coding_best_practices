# Order Processing: Bad vs. Good Code

## Problem Statement
An application needs to process customer and order data, ensuring proper validation and error handling. Poor implementations can lead to crashes, incorrect data handling, or unnecessary exits. Below, we compare bad versions of functions with optimized and error-resilient implementations.

## Order Processing

### Bad Code Example
The **bad code version** lacks proper validation and structured error handling, making it difficult to debug and maintain.

#### Issues in the Bad Code:
- ❌ **Assumes valid JSON input without validation**.
- ❌ **Uses `print` statements instead of logging**.
- ❌ **Does not handle division by zero properly**.
- ❌ **Catches generic exceptions instead of specific errors**.

#### Bad Code:
```python
import json

def process_order(order_data):
    try:
        order = json.loads(order_data)
        print("Processing order:", order["order_id"])
        
        if order["quantity"] == 0:
            print("Error: Quantity cannot be zero.")
            return
        
        if "total_price" not in order or "quantity" not in order:
            print("Error: Missing required order details.")
            return
        
        price_per_item = order["total_price"] / order["quantity"]
        print("Order processed successfully!")
    
    except json.JSONDecodeError:
        print("Error: Invalid JSON data.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except KeyError as e:
        print(f"Error: Missing required field {str(e)}.")
    except Exception as e:
        print(f"Something went wrong: {e}")
```

#### Testing:
```python
process_order('{"order_id": 123, "total_price": 100, "quantity": 0}')
```

### Good Code Example
The **good code version** improves error handling, logging, and robustness.

#### Key Improvements:
- ✅ **Uses structured logging instead of print statements**.
- ✅ **Handles JSON parsing errors properly**.
- ✅ **Implements custom exceptions for business logic validation**.
- ✅ **Ensures meaningful logging for better debugging**.

#### Good Code:
```python
import json
import logging

logging.basicConfig(
    filename="order_processing.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

class OrderProcessingError(Exception):
    pass

def process_order(order_data):
    try:
        order = json.loads(order_data)
        logging.info(f"Processing order: {order.get('order_id')}")
        
        if order["quantity"] == 0:
            raise OrderProcessingError("Quantity cannot be zero.")
        
        price_per_item = order["total_price"] / order["quantity"]
        logging.info(f"Order {order.get('order_id')} processed successfully.")
        return price_per_item
    
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON data: {e}")
    except ZeroDivisionError as e:
        logging.error(f"Math error in order processing: {e}")
    except OrderProcessingError as e:
        logging.warning(f"Order Processing Warning: {e}")
    except Exception as e:
        logging.exception(f"Unexpected error occurred: {e}")
```

#### Testing:
```python
process_order('{"order_id": 123, "total_price": 100, "quantity": 0}')
```

---

## Key Differences Between Bad and Good Code

| **Aspect**               | **Bad Code** 🛑                          | **Good Code** ✅                          |
|--------------------------|----------------------------------|----------------------------------|
| **Handling Missing Keys** | Uses `if "key" not in dict` and exits early | Uses `.get()` to provide default values |
| **Error Handling**       | Prints errors to the console, exits early | Uses fallback values for robustness |
| **Age/Quantity Validation** | Crashes on invalid input | Handles invalid data gracefully |
| **Logging**             | Uses `print` statements | Uses structured logging |
| **Code Readability**     | Harder to follow due to excessive conditions | Cleaner and more readable structure |

---

## Conclusion
The **Good Code** versions follow industry best practices, making the processing functions:
- 📌 **More readable** and maintainable.
- 📌 **Resilient to missing or invalid data**.
- 📌 **Scalable for future enhancements**.

Using **defensive programming** and structured validation improves code quality and prevents unexpected failures. 🚀

