"""
Given an int, figure out how many ones, threes and nines you could fit into the number. You must create a class. You will make variables (self.ones, self.threes, self.nines) to do this.

Examples
n1 = ones_threes_nines(5)
n1.nines ➞ 0
n1.ones ➞ 5
1.threes ➞ 1

Notes
Do not use the math module.
See version #2 of this series.
"""

class ones_threes_nines:
    def __init__ (self, n):
        self.ones = n // 1
        self.threes = n // 3
        self.nines = n // 9

n1 = ones_threes_nines(5)
print(n1.nines)
print(n1.threes)
print(n1.ones)
