"""
A repdigit is a positive number composed out of the
same digit. Create a function that takes an two-digit
integer and returns wwhether it's a repdigit or not.
"""


x = a = 4; b = 4;
y = a / b == 1

print(y)
# True


x = a = 4; b = 5;
y = a / b == 1

print(y)
# False


x = a = -4; b = 4;
y = a / b == 1

print(y)
# False