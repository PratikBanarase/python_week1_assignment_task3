# Problem 1 — Reverse a string
text = input("Enter a string: ")
print("Reversed:", text[::-1])

# Problem 2 — Count vowels
text = input("Enter a sentence: ")

vowels = "aeiou"
count = 0

for char in text.lower():
    if char in vowels:
        count += 1

print("Number of vowels:", count)

# Problem 3 — Check palindrome
text = input("Enter a string: ")

if text.lower() == text.lower()[::-1]:
    print("String is Palindrome")
else:
    print("String is not  palindrome")