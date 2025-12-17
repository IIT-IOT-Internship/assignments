from arithmatic import add, multiply
from string_ops import reverse_string, count_vowels

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", add(a, b))
print("Multiplication:", multiply(a, b))

text = input("Enter a string: ")

print("Reversed string:", reverse_string(text))
print("Vowel count:", count_vowels(text))