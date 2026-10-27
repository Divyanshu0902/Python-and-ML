with open("names.txt","r") as file:
    print(file.read())

# appending content to file: 
with open("names.txt","a") as file:
    file.write(" Prateek, Sanskar, Nirvick")
    
with open("names.txt","r") as file:
    print(file.read())