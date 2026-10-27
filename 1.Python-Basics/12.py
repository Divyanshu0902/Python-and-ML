'''
Write a Python program that accepts a string and counts the number of letters, digits, and special symbols.
'''

input_string = input("Enter the string: ")

letters = 0
digits = 0
symbols  = 0

for char in input_string:
    if char.isalpha():
        letters+=1

    elif char.isdigit():
        digits+=1
    else:
        if not (char.isspace()):
            symbols+=1

print(f"\nNo of alphabets: {letters}")
print(f"No of digits: {digits}")
print(f"No of special symbols: {symbols}\n")