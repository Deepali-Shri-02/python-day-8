num = (1,2,3,4,5,6,7)
a = int(input("Enter number to search:"))

if a in num:
    print(f"{a} found in tuple.")
else:
    print(f"{a} not found in tuple.")