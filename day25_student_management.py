# Day 25 - Mini Student Management System


students = {}


# -------------------------------
# Add Student
# -------------------------------

def add_student():

    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    students[name] = marks

    print("Student added successfully!")


# -------------------------------
# View Students
# -------------------------------

def view_students():

    if len(students) == 0:
        print("No student records found.")

    else:
        print("\nStudent Records:")

        for name, marks in students.items():
            print(f"{name} : {marks}")


# -------------------------------
# Search Student
# -------------------------------

def search_student():

    name = input("Enter student name to search: ")

    if name in students:
        print(f"{name}'s Marks: {students[name]}")

    else:
        print("Student not found.")


# -------------------------------
# Delete Student
# -------------------------------

def delete_student():

    name = input("Enter student name to delete: ")

    if name in students:
        del students[name]
        print("Student deleted successfully!")

    else:
        print("Student not found.")


# -------------------------------
# Main Menu
# -------------------------------

while True:

    print("\n===== Student Management System =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Program exited.")
        break

    else:
        print("Invalid choice. Try again.")
