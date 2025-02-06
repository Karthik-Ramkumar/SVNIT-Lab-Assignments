import re

sentence = input("Enter sentence to check if pangram or not: ").lower()
x = set(re.findall('[a-z]', sentence))
if len(x) == 26:
    print("Pangram")
else:
    print("Not a pangram")