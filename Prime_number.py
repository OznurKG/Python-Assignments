"""
Task:

Write a program that takes a number from the user and prints the result to check if it is a prime number.

Prime number means a number greater than 1, that is divisible only by itself and 1.

"""

number = int(input("Please enter a number: "))
for n in range(2, number):
    if number % n == 0:
        print(f"{number} is not a prime number")
        break
else:
    print(f"{number} is a prime number")
        


