with open("student.txt","r") as file:
    data = file.read()
words = data.split()


print("Number of words:",len(words))