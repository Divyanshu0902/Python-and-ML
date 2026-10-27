'''
Write a Python program that:
1. Opens numbers.txt in write mode.
2. Writes "10 20 30 40 50" to the file.
3. Closes the file automatically using with.
'''

# file = open("names.txt","w")
# file.write("Divyanshu, Ronak, Arka, Shashi, Rishabh")
# file.close()

## Opening a file :
with open("numbers.txt","w") as file:   
    file.write("10 20 30 40 50")

## Reading from a file :
with open("numbers.txt","r") as file:
    file_contents = file.read()

print(file_contents)
print(type(file_contents))

'''
Mode	Meaning
"w"	    Write; creates a file or overwrites its existing contents
"r"	    Read an existing file
"a"	    Append; adds content to the end of a file
'''


