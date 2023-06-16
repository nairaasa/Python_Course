"""Write a class called Name and create the following attributes given a first name and last name (as fname and lname):

An attribute called fullname which returns the first and last names.
An attribute called initials which returns the first letters of the first and last name. Put a . between the two letters.
Remember to allow the attributes fname and lname to be accessed individually as well.

Examples
a1 = Name("john", "SMITH")
a1.fname ➞ "John"

a1.lname ➞ "Smith"

a1.fullname ➞ "John Smith"

a1.initials ➞ "J.S"
Notes
Make sure only the first letter of each name is capitalised.
Check the Resources tab for some helpful tutorials on Python classes.
"""

class Name:
    def __init__(self, fname, lname):
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()
        self.fullname = fname.capitalize() + " " + lname.capitalize()
        self.initials = f"{fname.capitalize()[0]}.{lname.capitalize()[0]}"

a1 = Name("john", "SMITH")

print(a1.fname) 
print(a1.lname) 
print(a1.fullname)
print(a1.initials)