def strlen(str):
    len = 0
    for ch in str:
        len+=1
    return len

str = input("Enter string : ")

len = strlen(str)

print(f"Length = {len}")
