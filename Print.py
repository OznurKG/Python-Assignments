"""
Fill in the blanks to complete the program that prints all elements of the flowers list below each on separate lines such as : 

Rose 
Orchid 
Tulip 

Note: Use while loop.

"""

flowers = ['Rose', 'Orchid', 'Tulip']
count1 = len(flowers)
count2 = 0

while count1 > 0 :
    print(flowers[count2])
    count1 -= 1
    count2 += 1
