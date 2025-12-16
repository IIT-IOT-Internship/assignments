def overlapping(list1, list2):
    return bool(set(list1) & set(list2))

# Taking input from user
list1 = input("Enter elements of first list (space separated): ").split()
list1 = input("Enter elements of second list (space separated): ").split()

# Checking overlap
result = overlapping(list1, list1)


# Output
if result:
    print("True : The lists have at least one common element")
else:
    print("False : The lists do not have any common element")


list1 = input("Enter elements of first list (space separated): ").split()
list1 = input("Enter elements of second list (space separated): ").split()

