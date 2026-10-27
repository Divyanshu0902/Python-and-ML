'''
Write a function count_vowels(word) that:
1. Accepts a string.
2. Counts the vowels a, e, i, o, u, ignoring case.
3. Returns the count instead of printing it inside the function.

'''

def count_vowels(word):
    vowels = ['a','e','i','o','u']
    word_lower = word.lower()
    count = 0

    for char in word_lower:
        if char in vowels:
            count+=1

    return count

word = input("Enter a word: ")
count = count_vowels(word)
print(f"Number of vowels in the word '{word}': ",count)