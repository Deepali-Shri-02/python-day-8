with open("student.txt","r") as file:
    data = file.read()
    print(f"Number of characters in the file: {len(data)}")