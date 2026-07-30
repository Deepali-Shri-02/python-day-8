file = open("student.txt","r")

text = file.read()

word = input("enter word to search:")

if word in text:
    print("Word found")
else:
    print("Not found")

file.close()