# recursion

'''
Write a recursive function in Python to accept a number (variable num)
 and find the sum of all numbers in the range [0 - num]
'''

def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n-1)

n = int(input("Enter the number: "))
result = sum_numbers(n)

print(f"The sum of first {n} integers is: {result}")