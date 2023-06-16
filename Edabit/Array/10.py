"""
Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).

Examples
majority_vote(["A", "A", "B"]) ➞ "A"

majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"

majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None
Notes
The frequency of the majority element must be strictly greater than 1/2.
If there is no majority element, return None.
If the list is empty, return None.

"""

def majority_vote(lst):
    if len(lst) == 0:
        return None
    counts = {}
    for elem in lst:
        if elem not in counts:
            counts[elem] = 0
        counts[elem] += 1
    for elem, count in counts.items():
        if count > len(lst) / 2:
            return elem
    return None

print(majority_vote(["A", "A", "B"]))
# Output A
print(majority_vote(["A", "A", "A", "B", "C", "A"]))
# Output A
print(majority_vote(["A", "B", "B", "A", "C", "C"]))
# Output None