# 6. Create a function that takes a string
# txt and a number n and returns the repeated
# string n number of times.If given argument 
# txt is not a string, return Not A String !!

# Examples
# "Mubashir", 2 ➞ "MubashirMubashir"
# "Matt", 3 ➞ "MattMattMatt"
# 1990, 7 ➞ "Not A String !!"

x = "Mubashir" * 2
y = (x != str) * "Not A String !!" and (x == str) * x

print(y)
# This code didn't work...
