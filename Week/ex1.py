"""
1. Given a list, rotate the values clockwise by one
(the last value is sent to the first position).
Check the examples for a better understanding.

Examples
[1, 2, 3, 4, 5] ➞ [5, 1, 2, 3, 4]
[6, 5, 8, 9, 7] ➞ [7, 6, 5, 8, 9]
[20, 15, 26, 8, 4] ➞ [4, 20, 15, 26, 8]
"""

# x = [1, 2, 3, 4, 5]
# x[4] + x[0:]
# print(x[4] + x[0:4])
list =[20, 15, 26, 8, 4]
n = 1
list = (list[len(list) - n:len(list)] + list[0:len(list) - n])

print(list)
# 