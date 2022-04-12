#Write a short Python program that asks the user to enter Celsius temperature (it can be a decimal number), converts the entered temperature into Fahrenheit degree and prints the result.

celsius = input("Please enter the temperature in degree Celsius: ")
fahrenheit = float(celsius) * 9 / 5 + 32  # 0°C = 32°F
print(fahrenheit)