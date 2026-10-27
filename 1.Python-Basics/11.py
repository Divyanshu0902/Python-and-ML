# ***string methods***

## isalpha() — checks for letters

# Returns True if the string contains only alphabetic characters and has at least one character.
# print("Hello".isalpha()) #true
# print("Hello123".isalpha()) # False
# print("Hello World".isalpha()) # False


## isdigit() — checks for digits

# Returns True if all characters are digits and the string is non-empty.
# print("1234".isdigit()) #True
# print("1.23".isdigit()) #False
# print("12a3".isdigit()) #False


## isalnum() — checks for letters or digits

# Returns True if all characters are letters or digits, with at least one character.
# print("Hello123".isalnum())  # True
# print("Hello 123".isalnum()) # False
# print("Hello@123".isalnum()) # False


## isspace() — checks for whitespace

# Useful when you want to distinguish spaces from special symbols.
# print(" ".isspace())   # True
# print("\t".isspace()) # True
# print("A".isspace())   # False


## lower() and upper() — change letter case

# name = "Divyanshu Kumar"
# print(name.lower()) # divyanshu kumar
# print(name.upper()) # DIVYANSHU KUMAR


## count() — counts occurrences of a substring

# text = "banana"
# print(text.count("a"))   # 3
# print(text.count("an"))  # 2


## split() — converts a string into a list

# names_string = "Divyanshu Ronak Shashi Rhishabh Arka"
# print(names_string) # Divyanshu Ronak Shashi Rhishabh Arka
# names_list = names_string.split()
# print(names_list)  # ['Divyanshu', 'Ronak', 'Shashi', 'Rhishabh', 'Arka']


## find() — finds the position of a substring

# text = "Divyanshu Kumar"
# print(text.find("Divyanshu")) # 0
# print(text.find("Kumar")) # 10
# print(text.find("m")) # 12
# print(text.find("Rohit")) # -1


## replace() - replace a substring

# string = "I like Python very much!"
# new_string = string.replace("Python","Javascript")
# print(new_string)