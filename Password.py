"""
Task : Let's say; you left a message in the past that prints a password you need. 
To see the password you wrote, you need to enter your name and the program should recognize you. 

Write a program that :

Takes the first name from the user and compares it to yours, 
Then if the name the user entered is the same as yours, 
print out such as : "Hello, Joseph! The password is : W@12", 
If the name the user entered is not the same as yours, 
print out such as : "Hello, Amina! See you later."

"""

#First solution:

my_name = "Joseph"
password = "W@12"
name = input("Please enter your name: ")
print(my_name==name and "Hello, Joseph! The password is: W@12" or (f"Hello, {name}! See you later."))

#Second Solution:
 
my_name = "Joseph"
password = "W@12"
name = input("Please enter your name: ")
if name == my_name :
    print(f"Hello, {my_name}! The password is: {password}")
else :
    print(f"Hello, {name}! See you later.")


