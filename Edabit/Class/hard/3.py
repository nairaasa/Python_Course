"""
Create a class that imitates a select screen. For simplicity, the cursor can only move right!

In the display method, return a string representation of the list, but with square brackets around the currently selected element. Also, create the method to_the_right, which moves the cursor one element to the right.

The cursor should start at index 0.

Examples
menu = Menu([1, 2, 3])
menu.display() ➞ "[[1], 2, 3]"
menu.to_the_right()
menu.display() ➞ "[1, [2], 3]"

menu.to_the_right()
menu.display() ➞ "[1, 2, [3]]"

menu.to_the_right()
menu.display() ➞ "[[1], 2, 3]"
Notes
The cursor should wrap back round to the start once it reaches the end.
"""

class Menu:
    def __init__(self, lst):
        self.lst = lst
        self.position = 0
        self.len_lst = len(lst)
    
    def to_the_right(self):
        self.position = (self.position + 1) % self.lst
    
    def display(self):
        

menu = Menu([1, 2, 3])
print(menu.display())  # Output: "[[1], 2, 3]"

menu.to_the_right()
print(menu.display())  # Output: "[1, [2], 3]"

menu.to_the_right()
print(menu.display())  # Output: "[1, 2, [3]]"

menu.to_the_right()
print(menu.display())  # Output: "[[1], 2, 3]"
