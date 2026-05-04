# Day 14 - OOP (Classes & Objects) 🚀

# Creating a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} 👋"


# Creating object
p1 = Person("Abdul", 20)

print(p1.name)
print(p1.age)
print(p1.greet())


# Another class example
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"


s1 = Student("Rahman", 85)

print("\nStudent:", s1.name)
print("Marks:", s1.marks)
print("Grade:", s1.get_grade())


# Updating object data
s1.marks = 92
print("\nUpdated Marks:", s1.marks)
print("New Grade:", s1.get_grade())
