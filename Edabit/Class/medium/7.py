"""
Write a Composer class that has three instance variables:

name
dob
country
Add an additional class variable .count which counts the total number of instances created.

Examples
# Just finished writing the Composer class
Composer.count ➞ 0

c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
Composer.count ➞ 1

c2 = Composer("Wolfgang Amadeus Mozart", 1756, "Austria")
c3 = Composer("Johannes Brahms", 1833, "Germany")
Composer.count ➞ 3
Notes
N/A
"""

class Composer:
    count = 0
    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob
        self.country = country
        Composer.count += 1

print(Composer.count)
# Output 0
c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
print(Composer.count)

c2 = Composer("Wolfgang Amadeus Mozart", 1756, "Austria")
print(Composer.count)

c3 = Composer("Johannes Brahms", 1833, "Germany")
print(Composer.count)
