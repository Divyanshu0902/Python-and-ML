"""
Question 2 — Generate random numbers and write to a file
Question: Generate n random numbers in the range 60–90. Write them to a file, read and display its contents,
 and display the maximum and minimum values.
"""


import random

n = int(input("Enter number of random numbers: "))

numbers = [random.randint(60, 90) for _ in range(n)]

with open("numbers.txt", "w") as file:
    file.write("\n".join(map(str, numbers)))

with open("numbers.txt", "r") as file:
    content = file.read()

print("File contents:")
print(content)

if numbers:
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
