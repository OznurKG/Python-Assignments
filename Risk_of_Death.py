"""
Estimating the risk of death from coronavirus.

Consider the following questions in terms of True/False regarding anyone else.

Are you a cigarette addict older than 75 years old? Variable → age

Do you have a severe chronic disease? Variable → chronic

Is your immune system too weak? Variable → immune

Set a logical algorithm using boolean logic operators (and/or) and the given variables in order to 
give us True (there is a risk of death) or False (there is not a risk of death) as a result. 

age = # can be assigned only True/False 
chronic = # can be assigned only True/False 
immune = # can be assigned only True/False 
risk = ? (True or False)

"""

#Basic solution:

age = False
chronic = True
immune = True

risk = chronic or immune or age
print(risk)

#Other solution: Here, we get the answers from the user, and determine whether there is a detah risk or not.

age = input("You're a cigarette addict older than 75?: ") # Enter only "Yes" or "No"
chronic = input("You have a severe chronic disease?: ")
immune = input("Your immune system is too weak?: ")

if age.capitalize() == "Yes" :   #To prevent errors due to the typing, we use the capitatize func.
    age = True
else : 
    age = False
if chronic.capitalize() == "Yes" :
    chronic = True
else :
    chronic = False
if immune.capitalize() == "Yes" :
    immune = True
else :
    immune = False
if chronic and immune and age:
    print("You are in risky group")
else :
    print("You are not in risky group")


