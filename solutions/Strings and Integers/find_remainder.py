#!/usr/bin/env checkio --domain=py run find-remainder

# Determine the remainder from division of two positive integers.
# 
# 
# 
# Input:Two integers(int): dividend (the number to be divided) and divisor (the number by which division is going to be performed).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert find_remainder(10, 3) == 1
# assert find_remainder(14, 4) == 2
# assert find_remainder(27, 4) == 3
# assert find_remainder(10, 5) == 0
# Precondition:dividend, divisor > 0.
# 
# 
# END_DESC

a, b = 10, 3
c = a//b
d = a%b
print(c)
print(d)