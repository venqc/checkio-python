# Number gussing game
import random as rd 
print("Welcome! to the Number gussing game.")
low = int(input("low limit: "))
high = int(input("high limit: "))

x = rd.randint(low, high)
print(x)