source = open("student.txt","r")

content = source.read()

destination = open("backup.txt","w")

destination.write(content)

source.close()
destination.close()

print("File copied successfully.")