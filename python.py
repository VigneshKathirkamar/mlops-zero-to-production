# 1. Print text
print("Hello, World!")

# 2. Variables
name = "Alex"
age = 20
print(name)
print(age)

# 3. User input
name = input("Enter your name: ")
print("Hello,", name)

# 4. Basic calculations
a = 10
b = 5

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division

# 5. If-else
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")

# 6. For loop
for i in range(1, 6):
    print(i)

# 7. While loop
count = 1

while count <= 5:
    print(count)
    count += 1

# 8. List
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

# 9. Function
def greet(name):
    print("Hello,", name)

greet("Alex")
