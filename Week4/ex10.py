"""
10. Create a function that takes a list of numbers
lst, a string s and return a list of numbers as per the
following rules:
"Asc" returns a sorted list in ascending order.
"Des" returns a sorted list in descending order.
"None" returns a list without any modification.

Examples
[4, 3, 2, 1], "Asc"  ➞ [1, 2, 3, 4]
[7, 8, 11, 66], "Des" ➞ [66, 11, 8, 7]
[1, 2, 3, 4], "None" ➞ [1, 2, 3, 4]
"""
x, y = [1, 2, 3, 4], "Asc"
# y = (sorted(x), [-1], [:])
# z = (sorted(x), reverse= y ), 
# print(x)
print(
(y == "Asc") * sorted(x) +
(y == "Des") * sorted(x, reverse= True) +
y == "None"
)

