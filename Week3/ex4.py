"""
4. Luke Skywalker has family and friends. Help him
remind them who is who. Given a string with a name,
return the relation of that person to Luke.

Person  Relation
Darth Vader father
Leia    sister
Han brother in law
R2D2    droid

Examples
"Darth Vader" ➞ "Luke, I am your father."
"Leia" ➞ "Luke, I am your sister."
"Han" ➞ "Luke, I am your brother in law."
"""

name = input("Enter name: ")
x = "Luke, I am your "
y = ("father." * (name == "Darth Vader")) + ("sister." * (name == "Leia")) + ("brother in law." * (name == "Han")) + ("droid." * (name == "R2D2"))

print(x + y)
