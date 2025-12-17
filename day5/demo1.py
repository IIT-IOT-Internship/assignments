import math
import os

print("---- MATH MODULE ----")

num = int(input("Enter a number: "))

print("Square root:", math.sqrt(num))
print("Power (num²):", math.pow(num, 2))
print("Factorial:", math.factorial(num))
print("Value of Pi:", math.pi)

print("\n---- OS MODULE ----")

print("Current Working Directory:")
print(os.getcwd())

print("\nFiles and folders in this directory:")
print(os.listdir())

print("\nProgram executed successfully!")