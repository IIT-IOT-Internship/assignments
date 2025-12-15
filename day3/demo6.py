# Functions for basic arithmetic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


# Calculate function that takes another function as argument
def calculate(operand1, operand2, operation):
    return operation(operand1, operand2)


# Testing the calculate function with different inputs
print("Addition:", calculate(20, 10, add))
print("Subtraction:", calculate(20, 10, subtract))
print("Multiplication:", calculate(20, 10, multiply))
print("Division:", calculate(20, 10, divide))
print("Division by Zero:", calculate(20, 0, divide))
