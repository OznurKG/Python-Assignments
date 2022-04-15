"""
Task : Find out the most frequent number and its frequency.

Write a program that;

Finds out the most frequent number in the given list. Calculates its frequency. Prints out the result such as : 

Example Given list numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3] 
Desired Output: The most frequent number is 3 and it was 5 times repeated.

Note : You may need to use useful/necessary built-in functions and list methods.

"""

numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3, 5, 3,7]
most_frequent = max(numbers, key = numbers.count)
repetition = numbers.count(most_frequent)
print(f"The most frequent number is {most_frequent} and it was {repetition} times repeated")

