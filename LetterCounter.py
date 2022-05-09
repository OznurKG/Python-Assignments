"""
Count the number of each letter in a sentence.

Write a Python program that;

takes a sentence from the user, counts the number of each letter/chars of the sentence, collects the letters/chars as a key and the counted numbers as a value in a dictionary.

"""

def counter(input): 
    count_dict = {}
    for i in input.lower():
      count_dict[i] = input.lower().count(i)
    return count_dict
sentence = input()
print(counter(sentence))

