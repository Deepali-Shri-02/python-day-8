#Even and Odd list
l = [76,87,34,21,556,7568,8965,331,576]

en= []
on = []

for i in l:
    if i % 2 == 0:
        en.append(i)
    else:
        on.append(i)
print("Even",en)       
print("Odd",on)