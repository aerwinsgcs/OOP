class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # data members
        self.name = name
        self.salary = salary
        self.project = project

    # method to display employee's details
    def show(self):
        # accessing public data member
        print(self.name, 'earns a salary of: $', self.salary)

    # method (instance)
    def work(self):
        print(self.name, 'is working on', self.project)

# creating object of a class
emp = Employee('Jessa', 132000, 'Geosearching')

# calling method of the class
emp.show()
emp.work()
