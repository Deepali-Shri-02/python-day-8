with open("student.txt","r") as source:
    data = source.read()

with open("backup.txt","w") as destination:
    destination.write(data)

print("file copied successfully.")