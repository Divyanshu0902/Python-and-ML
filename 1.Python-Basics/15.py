# Random Password Generation :

'''
Generate a random password satisfying these conditions:
1. The password must be 10 characters long.
2. It must contain at least 2 uppercase letters, 1 digit, and 1 special symbol.
3. Create a list of the password's characters and check whether @ is present. 
If not, replace the third character with @.
4. Print the list as a single string using join()
'''

import random
import string

password = []
password.append(random.choice(string.ascii_uppercase))
password.append(random.choice(string.ascii_uppercase))
password.append(random.choice(string.digits))
password.append(random.choice(string.punctuation))

all_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
remaining_part = random.sample(all_characters,6)
for char in remaining_part:
    password.append(char)

random.shuffle(password)

contains_at_the_rate = False
for char in password:
    if char == '@':
        contains_at_the_rate = True
if not contains_at_the_rate:
    password[2] = '@'

final_password = "".join(password)
print("\nRandomly Generated Password: ",final_password,"\n")