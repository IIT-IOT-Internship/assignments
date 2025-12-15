num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

print("1. Add")
print("2. Sub")
print("3. Mul")
print("4. div")
choice = int(input("Enter your choice : "))

if(choice == 1):
    print(f"{num1} + {num2} = {num1 + num2}")
elif(choice == 2):
    print(f"{num1} - {num2} = {num1 - num2}")
elif(choice == 3):
    print(f"{num1} * {num2} = {num1 * num2}")
elif(choice == 4):
    print(f"{num1} / {num2} = {num1 / num2}")
