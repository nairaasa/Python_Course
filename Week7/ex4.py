"""
4. Create a function that takes the month and year (as integers) and
returns the number of days in that month.

Examples
days(2, 2018) ➞ 28
days(4, 654) ➞ 30
days(2, 200) ➞ 28
days(2, 1000) ➞ 28
Notes
Don't forget about leap years!
"""
def days(month, year):
    leap_year = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True
                if month == 2:
                    if leap_year:
                        return 29
                else:
                    return 28
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 31

print(days(2, 2018))


    
