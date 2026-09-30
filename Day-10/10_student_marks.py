marks = []
for i in range(5):
    mark = int(input("Enter marks for student {}: ".format(i+1)))
    marks.append(mark)  

total = sum(marks)
average = total/len(marks)
maximum = max(marks)
minimum = min(marks)

print("Total marks:", total)
print("Average marks:", average)
print("Maximum marks:", maximum)
print("Minimum marks:", minimum)
