'''
Using Python:
1. Consider n random numbers in the range 0.345 to 0.567.
2. Write the numbers to a file.
3. Open the file in read mode and display its contents.
4. Display the average value of the numbers.
5. Pass that average value to a function that calculates the area of a square.
'''

import random

def square(n):
    return n*n


n = int(input("\nEnter the value of n: "))

numbers = []

for i in range(n):
    number = random.uniform(0.345 , 0.567)
    numbers.append(number)
numbers_string = " ".join(map(str,numbers))

with open("file.txt","w") as file:
    file.write(numbers_string)

with open("file.txt","r") as file:
    content = file.read()
    print(content)
content_list = list(map(float,content.split(" ")))

average = sum(content_list)/len(content_list)

print("Average of all numbers: ",average)
print("Square: ", square(average))
