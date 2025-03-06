"""
Problem Statement:
In a financial application, we need to process transactions (such as credit and debit operations), check if the transaction is successful based on the updated balance, and calculate loan details like the loan amount, interest, and term. We also need to ensure the code is readable, maintainable, and follows industry-standard coding best practices.
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
