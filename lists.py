# Problem 1 — Largest and smallest
numbers = [10, 5, 20, 8, 15]
print("Largest:", max(numbers))
print("Smallest:", min(numbers))

# Problem 2 — Remove duplicates 
numbers = [4, 7, 2, 7, 9, 2]
unique_numbers = list(set(numbers))
print(unique_numbers)

# Problem 3 — Count even and odd
numbers = [1, 2, 3, 4, 5, 6]
even = 0
odd = 0
for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even number count is:", even)
print("Odd number count is:", odd)