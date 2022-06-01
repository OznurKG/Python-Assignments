"""
Given a list, return the most frequent (repeating) element. 

Note : If there are the same number of repeating elements, it returns the first element that repeats most from left to right in the list.

"""

def most_freq(given_list):
   return max(given_list, key = given_list.count)


given_list = [3,1,2,1,3]

print(most_freq(given_list))

Output: 3 

#If there is two numbers that repeated at the same times, the first will be displayed. Here, it is 3.