n = []
print("Enter 10 no.")
for i in range(10):
    num = int(input(f"Enter number {i + 1} : "))
    n.append(num)

s = sum(n)
average = s / 10

ec = 0
oc = 0

for x in n:
    if x % 2 == 0:
        ec += 1
    else:
        oc += 1

al = sorted(n)
dl = sorted(n, reverse = True)

print("\n-----Results-----")
print("List",n)
print("Largest no.",max(n))
print("Smallest no.", min(n))
print("Sum",s)
print("Average", average)
print("Even", ec)
print("Odd", oc)
print("Ascending",al)
print("Descending",dl)
            