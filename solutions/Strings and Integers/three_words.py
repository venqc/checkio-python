#!/usr/bin/env checkio --domain=py run three-words

# Let's teach the Robots to distinguish words and numbers.
# 
# You are given a string with words and numbers separated by whitespaces (one space).    The words contain only letters.    You should check if the string contains three words insuccession.    For example, the string "start 5one two three7 end" contains three words in succession.
# 
# 
# 
# Input:A string(str)with words.
# 
# Output:Logic value(bool).
# 
# Precondition:The input contains words and/or numbers. There are no mixed words (letters and digits combined).
# 0 < len(words) < 100
# 
# 
# END_DESC

def checkio(words: str) -> bool:
    # add your code here
    return False


print("Example:")
print(checkio("Hello World hello"))

# These "asserts" are used for self-checking
assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")