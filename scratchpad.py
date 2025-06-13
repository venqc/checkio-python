# Number guessing game
import random as rd 
print("Welcome! to the Number guessing game.")
low = int(input("low limit: "))
high = int(input("high limit: "))

x = rd.randint(low, high)
print(x)
print(x +3)