#!/usr/bin/env checkio --domain=py run is-even

# Check if the given number is even or not. Your function should returnTrueif the number is even, andFalseif the number is odd.
# 
# Input:An integer(int).
# 
# Output:Logic value(bool).
# 
# 
# END_DESC

def is_even(num: int) -> bool:
    # your code here
#    return not num % 2
     return num & 1 == 0

print("Example:")
print(is_even(2))

# These "asserts" are used for self-checking
assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")