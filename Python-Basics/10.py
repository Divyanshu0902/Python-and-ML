# list reversal

'''
Write a function in Python to print a list of numbers in reverse order
'''

names = input("\nEnter the names: ").split(", ")
reverse = []

for i in range(len(names)):
    name = names[-(i+1)]
    reverse.append(name)

print("\nOriginal List: ", names)
print("Reversed List: ", reverse, "\n")