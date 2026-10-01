import random

#key---> value
emoji = {"R":"🪨", "S":"✂️" , "P":"📃"}
choice = ("R","P","S")  #tuple(read only list)

while True:
    customer_choices = input("Rock, Paper or Scissor(R,P,S): ").upper()

    # if customer_choices !="R" and customer_choices !="P" and customer_choices !="S":   ----> works but not a professional way to implement

    if customer_choices not in choice:
        print("Enter Valid item")
        continue  #to resolve the crash

    computer_choice = random.choice(choice)

    #print("My choice: " + customer_choices)   ---> works
    #adding emojies
    """if customer_choices == "R":
        print("🪨")
    elif customer_choices == "S":
        print("✂️")"""

    print(f"My choice: {emoji[customer_choices]}") 
    #print(f"My choice: {customer_choices}")   #without concatination, emoji
    print(f"Computer choice: {emoji[computer_choice]}")

    if customer_choices == computer_choice:
        print("Its a Tie!!")
        """elif customer_choices == "R" and computer_choice == "S":
        print("You win!!")
        elif customer_choices == S" and computer_choice == "P":
        print("You Win!!")"""

        #elif (customer_choices == "R" and computer_choice == "S") or (customer_choices == "S" and computer_choice == "P") or (customer_choices == "P" and computer_choice == "R"):
        
        """elif \
        (customer_choices == "R" and computer_choice == "S") or\
        (customer_choices == "S" and computer_choice == "P") or \
        (customer_choices == "P" and computer_choice == "R"):
        """
    elif ((customer_choices == "R" and computer_choice == "S") or
        (customer_choices == "S" and computer_choice == "P") or 
        (customer_choices == "P" and computer_choice == "R")):
        print("You win!!")
    else:
        print("You Lose!!")


    ##ask user to continue

    #continue ---> we can't use continue because its a reserved keyword
    should_continue = input("Another Round (Y/N): ").lower()
    if should_continue == "n":
        break