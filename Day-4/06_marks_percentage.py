s1 = float(input("Maths marks: "))
s2 = float(input("Science marks: "))
s3 = float(input("English marks: "))
s4 = float(input("History marks: "))
s5 = float(input("Geography marks: "))

total = s1 + s2 + s3 + s4 + s5
percentage = total / 5
average = total / 5
print("\n ----------Marks Percentage----------\n")
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Average:", average)