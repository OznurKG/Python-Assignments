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
        
#Second solution:

n = int(input("Enter a positive int number to check if it is a Prime Number."))

counter = 0

for i in range(1, n+1) :
    if n % i == 0 :
        counter += 1
        
if (n == 0) or (n == 1) or (counter >= 3) :
    print(n, " is not a Prime Number.")
    
else :
    print(n, " is a Prime Number.")

    
