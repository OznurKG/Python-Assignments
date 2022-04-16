### Task : Find out if the given word is "comfortable words" in relation to the ten-finger keyboard use.

# A comfortable word is a word which you can type always alternating the hand you type with (assuming you type using a Q-keyboard and use of the ten-fingers standard). 

# The word will always be a string consisting of only letters from a to z. 

# Write a program which returns True if it's a comfortable word or False otherwise. 

# Examples Given word 
# Desired Output (explanation) tester False (uses only left-hand fingers)* polly False (uses only right-hand fingers)* clarusway True (uses both hand fingers)

# Note : Do a quick research on ten-fingers keyboard usage. 
# () the explanation doesn't need to be in the output. 


#The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
left_hand = set("qazwsxedcrfvtgb")
right_hand = set("yhnujmıkolp")
word = set(input("Please enter a word: "))  

comfortable_word = not left_hand.isdisjoint(word) and not right_hand.isdisjoint(word)
print(comfortable_word)


#The intersection() method returns a set that contains the similarity between two or more sets.

right = set('yuiophjklnm')
left = set('qwertasdfgzxcvb')
test = set(input("Please enter a word: "))
comfortable_word = right.intersection(test) != "" and left.intersection(test) != ""
print(comfortable_word)


