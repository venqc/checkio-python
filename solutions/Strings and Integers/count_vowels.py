#!/usr/bin/env checkio --domain=py run count-vowels

# This function should take a string as an input and return the count of vowels (a, e, i, o, u) in the string. The function should be case-insensitive.
# 
# 
# 
# Input:String(str).
# 
# Output:Integer(int).
# 
# Examples:
# 
# assert count_vowels("hello") == 2
# assert count_vowels("openai") == 4
# assert count_vowels("typescript") == 2
# assert count_vowels("a") == 1
# Preconditions:text ∈ string;length(text) >= 0.
# 
# 
# END_DESC

def count_vowels(text: str) -> int:
    
    count = 0
    for char in text.lower():
        count += char in "aeiou"
    return count
print("Example:")
print(count_vowels("Hello"))

# These "asserts" are used for self-checking
assert count_vowels("hello") == 2
assert count_vowels("openai") == 4
assert count_vowels("typescript") == 2
assert count_vowels("a") == 1
assert count_vowels("b") == 0
assert count_vowels("aeiou") == 5
assert count_vowels("AEIOU") == 5
assert count_vowels("The quick brown fox") == 5
assert count_vowels("Jumps over the lazy dog") == 6
assert count_vowels("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")

# your code here
    #x = list(str.lower(text))
    #count = 0
    #if x[0::1] == 'e':
    #    count = count + 1
    #    return count
    #return count