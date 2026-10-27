# random module of python

import random 

## random.random()
# returns a floting point number from [0.00, 1.00)


## random.randint(a,b)
# returns one random integer between [a,b]
# print(random.randint(1,10))

## random.randrange(a,b,r)
# returns one integer from the range [a,b) with step 'r'
# print(random.randrange(2,12,2))

## random.choice(list)
# Selects one random element from a list.
# names = ["Divyanshu", "Arka", "Ronak", "Shashi","Rishabh", "Pratik"]
# print(random.choice(names))

## random.sample(list, k)
# Selects k unique elements without replacement.
# names = ["Divyanshu", "Arka", "Ronak", "Shashi","Rishabh", "Pratik"]
# print(random.sample(names,3))

## random.shuffle(list)
# shufles the original list
names = ["Divyanshu", "Arka", "Ronak", "Shashi","Rishabh", "Pratik"]
random.shuffle(names)
print(names)

