class Employee:

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)

emp1 = Employee("Abdul", "Python Learner")

emp1.display()
