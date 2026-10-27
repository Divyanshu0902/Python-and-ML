def Rect_Area(l,b):
    return l*b

def Multi(x):
    for i in range(1,11):
        print(x*i)

def Authenticate(a,b):
    ids = [101, 102, 103, 104, 105]
    passwords = ["a1x", "b2x", "c3y", "d4y", "e5z"]

    for i in range (len(ids)):
        if ids[i]==a and passwords[i]==b:
            return 1
    return 0
        
