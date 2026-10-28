# 5 random integers between 60 and 90

import random 

numbers = [random.randint(60,90) for _ in range(5)]
# print(numbers)
# with open("file2.txt","w") as file2:
#     file2.write(" ".join(map(str,numbers)))

with open("file2.txt","r") as file2:
    loaded_data = file2.read()

print(loaded_data)

n1 = loaded_data.split(" ")
n2 = list(map(int, n1))
# for value in n1:
#     n2.append(map(int,value))

print(n2)
print(max(n2))
print(min(n2))


# 5 random decimal numbers between 60 and 90
# numbers2 = [random.uniform(60,90) for _ in range(5)]
# print(numbers2)

