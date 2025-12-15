# Recursive function to find factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Recursive function to find power
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

# Main program (menu-driven)
while True:
    print("\n--- Menu ---")
    print("1. Find Factorial")
    print("2. Find Power")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))
        print("Factorial =", factorial(num))

    elif choice == 2:
        base = int(input("Enter base: "))
        exp = int(input("Enter exponent: "))
        print("Power =", power(base, exp))

    elif choice == 3:
        print("Program Ended")
        break

    else:
        print("Invalid choice")
