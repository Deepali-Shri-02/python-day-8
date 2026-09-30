students = ["Rahul", "Ramesh", "Suresh", "Mahesh"]

name = input("enter student name to search: ")

if name in students:
    print(f"{name} is present in the list at index {students.index(name)}")
else:
    print(f"{name} is not present in the list.")