'''
Write a program that accepts a list of names and prints, for each name:
1. Its length.
2. Its number of vowels.

'''

def count_vowels(word):
    vowels = ['a','e','i','o','u']
    word_lower = word.lower()
    count = 0

    for char in word_lower:
        if char in vowels:
            count+=1

    return count

n = int(input("Total How many names? : "))
names = []

for i in range(n):
    name = input(f"Enter name{i+1}: ")
    names.append(name)

print("")

for name in names:
    print(f"Name: {name} | length: {len(name)} | vowels: {count_vowels(name)}")