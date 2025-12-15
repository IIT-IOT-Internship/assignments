num = int(input("Enter number : "))

fact = 1
i = 1
while i <= num:
    fact *= i
    i+=1

print(f"{num}! = {fact}")
