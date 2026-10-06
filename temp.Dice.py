"""
do you want to roll the dice (y/n)
yes-random number
no- thank you message
any letter- chose (y or n)
"""
import random

while True:
    chose = input("Do you want to roll the dice(y/n): ")
    if chose.lower() =="y":
        add1 = random.randint(1,6)
        add2 = random.randint(1,6)
        print(f'({add1},{add2})')
    elif chose.upper()=="N":
        print("Thank you, Bye")
        break
    else:
        print("chose Y or N")