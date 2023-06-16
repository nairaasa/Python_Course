"""
8. Create a function that converts a date
formatted as MM/DD/YYYY to YYYYDDMM.

Examples
"11/12/2019" ➞ "20191211"
"12/31/2019" ➞ "20193112"
"01/15/2019" ➞ "20191501"
"""

x = "11/12/2019"
x = x.split("/")
year = (x[2])
month =(x[1])
day = (x[0])

print(year + month + day)