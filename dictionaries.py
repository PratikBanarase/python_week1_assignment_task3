# Problem 1 — Character frequency
text = "banana"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print(freq)

# Problem 2 — Find maximum value
marks = {
    "Neha": 91,
    "Arjun": 85,
    "Rahul": 88
}
highest_student = max( marks, key=marks.get)
print("Top student:", highest_student)

#Problem 3 — Student marks average
marks = {
    "Math": 90,
    "Python": 95,
    "SQL": 85
}
average = sum(marks.values()) / len(marks)
print("Average:", average)