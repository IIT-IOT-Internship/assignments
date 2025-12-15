s = input("Enter a string: ")
print("\nOriginal String:", s)

# Case conversion
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Title case:", s.title())

# Length of string
print("Length of string:",len(s))

# Checking methods
print("Is alphabetic?",s.isalpha())
print("Is digit?",s.isdigit())
print("Is alphanumeric?",s.isalnum())

# Searching
print("Count of 'a':",s.count('a'))
print("Index of 'a':",s.find('a'))

# Replace
print("Replace 'a' with '@':", s.replace('a', '@'))

# Removing spaces
print("After strip():",s.strip())

# Splitting and joining
words = s.split()
print("Split words:",words)
print("Joined with hyphen:", "-".join(words))
