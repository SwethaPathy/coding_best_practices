"""
Problem Statement:
In a financial application, we need to process transactions (such as credit and debit operations), check if the transaction is successful based on the updated balance, and calculate loan details like the loan amount, interest, and term. 
"""


def pt(t, a):
    x = 0
    for i in t:
        if i == "credit":
            x += a
        elif i == "debit":
            x -= a
    if x > 1000:
        print("Transaction completed")
    else:
        print("Transaction failed")
    return x


def qd(t):
    p = 100000
    l = 1000
    return p, l, 3000


# Run bad code example
transaction_types = ["credit", "debit", "credit"]
amount = 500

result = pt(transaction_types, amount)
print(f"Final Balance: {result}")

loan_details = qd(transaction_types)
print(f"Loan Details: {loan_details}")
