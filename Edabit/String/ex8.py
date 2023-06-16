class Employee:
    def __init__(self, fullname, email):
        self.fullname = fullname
        self.email = email

    def get_fullname():
        return f"{{self.fullname}}"
    
    def get_email():
        return f"{{self.email}}"

emp_1 = "John Smith"

print(emp_1.get_fullname)