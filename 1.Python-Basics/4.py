# check armstrong number

def is_armstrong(n):
    number = n
    total_digits = len(str(n))
    result = 0

    for i in range (1,total_digits+1):
        digit = n%10
        result = result + digit**total_digits
        n = int(n/10)

    if result == number :
        return True
    else:
        return False

n = int(input("Enter the number to check: "))

if is_armstrong(n):
    print(f"{n} is an Armstring Number")
else:
    print(f"{n} is not an Armstring Number")