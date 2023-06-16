"""Given a list of people objects, create a function that sorts the list by an attribute name. The attribute to sort by will be given as a string.

The Person class will only include these attributes in the following order:

firstname
lastname
age
Examples
p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)
people_sort([p1, p2, p3], "firstname") ➞ [p2, p1, p3]
# Alice, Michael, Zoey

people_sort([p1, p2, p3], "lastname") ➞ [p3, p1, p2]
# Jones, Smith, Waters

people_sort([p1, p2, p3], "age") ➞ [p2, p3, p1]
# 21, 29, 40
Notes
Sort the list in ASCENDING order.
All objects will be valid.
"""

# class Person:
#     def __init__(self, firstname: str = None, lastname: str = None, age: str = None):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
    
# def get_attr_value(person, attribute):
#         if attribute == "firstname":
#             return person.firstname
#         elif attribute == "lastname":
#             return person.lastname
#         elif attribute == "age":
#             return person.age
        
# def people_sort(people, attribute):
#         return sorted(people, key=lambda person: get_attr_value(person, attribute))

# p1 = Person("Michael", "Smith", 40)
# p2 = Person("Alice", "Waters", 21)
# p3 = Person("Zoey", "Jones", 29)

# sorted_by_firstname = people_sort([p1, p2, p3], "firstname")
# print(sorted_by_firstname)
# # Alice, Michael, Zoey

# sorted_by_lastname = people_sort([p1, p2, p3], "lastname")
# print(sorted_by_lastname)
# # Jones, Smith, Waters

# sorted_by_age = people_sort([p1, p2, p3], "age")
# print(sorted_by_age)
# # 21, 29, 40