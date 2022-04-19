"""
Task. If you had deposited a coin on the cryptocurrency exchange that brought 7% fixed profit daily for a week, 
how much would your $ 1000 reach at the end of the 7th day?"""

capital = 1000
rate = 0.07
capital = capital * (1 + rate)**7

print(f"Your $1000 will reach ${round(capital)} at the end of the 7th day.")

