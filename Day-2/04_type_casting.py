#Program1
age = int(input("Enter your age:"))
height = float(input("Enter your height:"))

print("Age:", age)
print("Height:", height)

print("\n"*2) 

#Program2 implicit type casting
x = 5
y = 2.0
z = x + y
print("Z:", z)
print("Type of Z:", type(z))

print("\n"*2)

#Program3 explicit type casting
a = 10
b = 3.5
c = int(b)  # Explicitly casting float to int
print("C:", c)
print("Type of C:", type(c))

print("\n"*2)

#Program4 
#string to integer
age =int("23")
#float to integer
pi_int = int(3.14)
#number to string
message = "Score: " + str(95)
has_items = bool([1,2,3])  # Non-empty list evaluates to True
is_empty = bool([""])  # Empty list evaluates to False

print("Age:", age)
print("Pi as integer:", pi_int)
print("Message:", message)
print("Has items:", has_items)
print("Is empty:", is_empty)
