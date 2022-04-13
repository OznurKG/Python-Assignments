"""
Write a short Python program that asks the user to enter a distance (it can be a decimal number) in kilometers, 
converts the entered distance into miles and prints the result."""


distance_km = input("Please enter a distance in km: ")  
distance_m = float(distance_km) * 0.621   # 1 km is equal to 0.621 miles
print(f"{distance_km} kilometers is equal to {distance_m} miles.")



