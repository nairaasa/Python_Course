"""
Write a function that takes the coordinates of three points in the form of a 2d array and returns the perimeter of the triangle. The given points are the vertices of a triangle on a two-dimensional plane.

Examples
perimeter([[15, 7], [5, 22], [11, 1]]) ➞ 47.08

perimeter([[0, 0], [0, 1], [1, 0]]) ➞ 3.41

perimeter([[-10, -10], [10, 10 ], [-10, 10]]) ➞ 68.28
Notes
The given points always create a triangle.
The numbers in the argument array can be positive or negative.
Output should have 2 decimal places
This challenge is easier than it looks.

"""

from math import sqrt

def perimeter(vertices):

    a = sqrt((vertices[1][0] - vertices[0][0])**2 + (vertices[1][1] - vertices[0][1])**2)
    b = sqrt((vertices[2][0] - vertices[1][0])**2 + (vertices[2][1] - vertices[1][1])**2)
    c = sqrt((vertices[0][0] - vertices[2][0])**2 + (vertices[0][1] - vertices[2][1])**2)
    
    return round(a + b + c, 2)

print(perimeter([[15, 7], [5, 22], [11, 1]]))

print(perimeter([[0, 0], [0, 1], [1, 0]]))

print(perimeter([[-10, -10], [10, 10 ], [-10, 10]]))