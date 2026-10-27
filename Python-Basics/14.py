'''
Find all occurrences of a substring in a given string by ignoring the case.
'''

string = input("\nEnter the string: ")
string_l = string.lower()
substring = input("Enter the substring to find: ")
substring_l = substring.lower()

occurences = string_l.count(substring_l)
print(f"\nNumber of occurences of {substring} in the given string is: {occurences}")