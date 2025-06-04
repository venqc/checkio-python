#!/usr/bin/env checkio --domain=py run convert-to-title-case

# Your function should take a string as an input and convert all the first letters of the words in the string to uppercase, making the string a title case (other letters must be in lowercase).
# 
# 
# 
# Input:Original string(str).
# 
# Output:Converted string(str).
# 
# Examples:
# 
# assert to_title_case("hello world") == "Hello World"
# assert to_title_case("openai gpt-4") == "Openai Gpt-4"
# assert to_title_case("this is a title") == "This Is A Title"
# assert to_title_case("THE QUICK BROWN FOX") == "The Quick Brown Fox"
# Preconditions:sentence ∈ string;length(sentence) >= 0.
# 
# 
# END_DESC

def to_title_case(sentence: str) -> str:
    # your code here
    lst = sentence.split()
    obj = map(str.capitalize, lst)
    z = ' '.join(obj)
    return z
    #


print("Example:")
print(to_title_case("hello world"))

# These "asserts" are used for self-checking
assert to_title_case("hello world") == "Hello World"
assert to_title_case("openai gpt-4") == "Openai Gpt-4"
assert to_title_case("this is a title") == "This Is A Title"
assert to_title_case("THE QUICK BROWN FOX") == "The Quick Brown Fox"
assert to_title_case("JUMPs ovER a LAZy dog") == "Jumps Over A Lazy Dog"
assert to_title_case("typescript is great") == "Typescript Is Great"
assert to_title_case("the answer is 42") == "The Answer Is 42"
assert to_title_case("to be or not to be") == "To Be Or Not To Be"
assert to_title_case("that is the question") == "That Is The Question"
assert to_title_case("") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")