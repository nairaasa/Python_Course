"""
EXTRA Knowledge
5. Given two strings, create a function that returns the total
number of unique characters from the combined string.

Examples
count_unique("apple", "play") ➞ 5
# "appleplay" has 5 unique characters:
# "a", "e", "l", "p", "y"
"sore", "zebra" ➞ 7
"a", "soup" ➞ 5
"""
str = "apple", "play"
result = len(dict.fromkeys(str))
print(result)