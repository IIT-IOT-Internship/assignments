
# 1. Function with default parameter value
def greet(name="Guest", message="Welcome"):
    print(message, name)


# 2. Functions for arithmetic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


# 3. Function that accepts another function as argument
def calculate(x, y, operation):
    return operation(x, y)


# ---- Function Calls ----

# Default parameter values
greet()
greet("Siddhi")
greet("Siddhi", "Hello")

print()

# Keyword arguments
greet(message="Good Morning", name="Siddhi")

print()

# Passing function to another function
result1 = calculate(10, 5, add)
result2 = calculate(10, 5, subtract)

print("Addition:", result1)
print("Subtraction:", result2)
