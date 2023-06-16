# 1. Emmy has written a function that returns a greeting
# to users. However, she's in love with Mubashir, and
# would like to greet him slightly differently. She added
# a special case in her function, but she made a mistake.

# Can you help her?

# Examples
# "Matt" ➞ "Hello, Matt!"
# "Helen" ➞ "Hello, Helen!"
# "Mubashir" ➞ "Hello, my Love!"

"""name = "Matt!"
greeting = "Hello, "
result = greeting + name

print(result)
# Hello, Matt!

name = "Mubashir!"
greeting = "Hello, "
mistake = "my love!"
special_case = greeting + mistake
expected_result = greeting + name

print(expected_result)
# Hello, Mubashir!"""


name = input("Enter name: ")
y = "Hello, " + name
x = "Hello, my love"

print(x * (name == "Mubashir") + y * (name != "Mubashir"))