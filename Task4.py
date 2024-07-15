import random
import string

userscore = 0
computerscore = 0

def regame():
    global userscore, computerscore
    
    choices = ['rock', 'paper', 'scissors']
    print("Enter your choice: rock, paper, or scissors")
    user_choice = input("Your choice: ").lower()
        
    while user_choice not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Your choice: ").lower()
    
    computer_choice = random.choice(choices)
        
    print(f"You chose: ",user_choice)
    print(f"Computer chose: ",computer_choice)
        
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
        userscore += 1
    else:
        result = "You lose!"
        computerscore += 1

    print(result)
    print("Score:")    
    print("You:", userscore)
    print("Computer:", computerscore)
    
    rg = input("Do you want to play again? (yes/no): ").lower()
    if rg == "yes":
        regame()
    else:
        rm = input("Do you want to restart match? (yes/no): ").lower()
        if rm == "yes":
            userscore = 0
            computerscore = 0
            regame()
        else:
            print("Thank you for playing!")

regame()
