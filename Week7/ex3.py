"""
3. Create a function that takes three values:
h hours
m minutes
s seconds
Return the value that's the longest duration.
Examples
longestTime(1, 59, 3598) ➞ 1
longestTime(2, 300, 15000) ➞ 300
longestTime(15, 955, 59400) ➞ 59400
"""

def longestTime(h, m, s):
    sec = h*3600 + m*60 + s
    return max(h, m, s, sec)

print(longestTime(1, 59, 3598))
print(longestTime(2, 300, 15000))
print(longestTime(15, 955, 59400))