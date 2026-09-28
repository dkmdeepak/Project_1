"""
guess the number between 1 and 100
if not -guess the number between 1 and 100
if<number - too low
if>number - too high
if yes - congradulation
if alphabet: please enther valid number
"""

import random

finding_number = random.randint(1,100)
while True:
    try:
        number = int(input("Guess the number between 1 and 100: "))
        
        if  number < finding_number:
            print("Too low") 
        elif number > finding_number:
            print("Too high")
        else:
            print("congradulation")
            break
    except ValueError:
        print("Enter Valied Number")