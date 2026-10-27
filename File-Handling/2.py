# read numbers from the file numbers.txt and print their sum

with open("numbers.txt","r") as file:
    num_string = file.read()

num_chars_list = num_string.split(" ")
numbers_list = list(map(int,num_chars_list))

print("The sum of the numbers in the file is: ", sum(numbers_list))