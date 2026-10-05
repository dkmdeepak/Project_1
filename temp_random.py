import random

find_number=random.randint(1,100)
while True:
    try:
        guess = int(input('Guess the number: '))    
        if guess > find_number:
            print("Too High!")
        elif guess < find_number:
            print("Too Low!")
        else:
            print("Congradulation!!!")
            break
    
    except ValueError:
        print("Enter number")
       