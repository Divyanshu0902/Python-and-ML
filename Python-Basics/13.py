'''
Given two strings, write a program that returns a new string made from
the first, middle, and last characters of both strings.
'''

s1 = input("\nEnter the first string: ")
s2 = input("Enter the second strng: ")

m1 = s1[len(s1)//2]
m2 = s2[len(s2)//2]

s3 = s1[0]+s2[0]+m1+m2+s1[-1]+s2[-1]

print("\nNew String: ", s3,"\n")