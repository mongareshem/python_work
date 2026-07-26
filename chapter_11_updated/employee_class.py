class Employee:
    def __init__(self, firstname, lastname, annual_salary):
        """Initialize attributes"""
        self.firstname = firstname
        self.lastname = lastname
        self.annual_salary = annual_salary

    def give_raise(self, increment=5_000):
        self.annual_salary += increment
        return self.annual_salary