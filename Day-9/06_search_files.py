word = input("enter the word to search: ")

with open("student.txt","r") as file:
    data = file.read()

if word.lower() in data.lower():
    print(f"{word} is present in the file.")
else:
    print(f"{word} is not present in the file.")    