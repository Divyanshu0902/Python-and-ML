"""
Write a Python code to generate 100 random lottery tickets number. The number in the ticket consist of 8 digits. 
Next, pick three lucky tickets from it and print the ticket number of the 3 winners.
"""

import random

tickets = []

for i in range(100):
    ticket = random.randint(10000000, 99999999)
    tickets.append(ticket)

winners = random.sample(tickets,3)
print("The winners are: \n",winners)