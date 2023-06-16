"""
5. Write a function that takes two
integers (hours, minutes), converts
them to seconds, and adds them.
1,3 ➞ 3780
2,0 ➞ 7200
"""



x = 1
y = 3
z = (x * 60**2) + (y * 60)

print(z)
# 3780


x = 2
y = 0
z = (x * 60**2) + (y * 60)

print(z)
# 7200