import random

#while True:
choice = input ("Roll the dice (y/n): ")

if choice.upper() == "Y":
        dice1 = random.randint(1,6) 
        dice2 = random.randint(1,6) 
        print(f'({dice1}, {dice2})')
elif choice.upper() == "N":
    print("Thank you")
      #  break
else:
    print("Invalid choice")