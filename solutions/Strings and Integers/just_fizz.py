#!/usr/bin/env checkio --domain=py run just-fizz

# You should write a function that will receive a positive integer and return:"Fizz"if the number is divisible by 3 (3, 6, 9 ...) otherwise convert the given number to a string (2->"2").
# 
# 
# 
# Input:An integer(int).
# 
# Output:A string(str).
# 
# Examples:
# 
# assert checkio(15) == "Fizz"
# assert checkio(6) == "Fizz"
# assert checkio(10) == "10"
# assert checkio(7) == "7"
# 
# END_DESC

def checkio(num: int) -> str:
    # your code here
    if not num % 3:
        return "Fizz"
    else:
        return str(num)


print("Example:")
print(checkio(3))

# These "asserts" are used for self-checking
assert checkio(15) == "Fizz"
assert checkio(6) == "Fizz"
assert checkio(10) == "10"
assert checkio(7) == "7"

print("The mission is done! Click 'Check Solution' to earn rewards!")