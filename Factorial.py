"""
Define a function named my_fact to calculate factorial of the given number. 

Given a non-negative integer return the factorial of the integer.

"""

def my_fact(n):
  factorial = 1
  if n < 0:
    n *= -1
  for i in range(1, n+1):
    factorial *= i
  return factorial


