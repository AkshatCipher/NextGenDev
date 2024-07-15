# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    else:
        return x / y

print("Operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

ch = int(input("Enter operation choice (1/2/3/4): "))
if ch not in (1, 2, 3, 4):
    print("Invalid input. Please Restart!")
else:

    if ch == 1:
        result = add(num1, num2)
    elif ch == 2:
        result = subtract(num1, num2)
    elif ch == 3:
        result = multiply(num1, num2)
    elif ch == 4:
        result = divide(num1, num2)

    print("Result:", result)