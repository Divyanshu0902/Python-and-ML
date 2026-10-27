'''
Write a program that:
1. Accepts a paragraph from the user using input().
2. Writes the paragraph to r1.txt.
3. Reads and prints the contents of r1.txt.
4. Copies the contents into r2.txt.
5. Reads and prints the contents of r2.txt.
'''

user_input = input("\nEnter a paragraph: ")

with open("r1.txt","w") as r1:
    r1.write(user_input)

with open("r1.txt","r") as r1:
    r1_content = r1.read()
    print("\nContents of file r1: ",r1_content)

with open("r2.txt","w") as r2:
    r2.write(r1_content)

with open("r2.txt","r") as r2:
    r2_content = r2.read()
    print("Contents of file r2: ",r2_content,"\n")