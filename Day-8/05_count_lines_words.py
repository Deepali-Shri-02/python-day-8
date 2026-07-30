file = open("student.txt","r")

text = file.read()

lines = text.split("\n")
words = text.split()

print("Total lines:",len(lines))
print("Total Words:",len(words))