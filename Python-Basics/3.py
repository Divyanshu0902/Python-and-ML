# prime numbers in a range

def is_prime(n):
    if n<2:
        return False

    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def prime(start, end):
    for j in range (start, end+1):
        if is_prime(j):
            print(j)

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
prime(start, end)