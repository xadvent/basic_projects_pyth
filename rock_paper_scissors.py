import random
import os

list_of_choices = ["rock", "paper", "scissors"]

def comp():
    competition = random.choice(list_of_choices)
    return competition

def get_guess():
    while True:
        guess = input("Type 1 for Rock, 2 for Paper and 3 for Scissors: " )
        if guess.isdigit():
           guess = int(guess) - 1
           choice = list_of_choices[guess]
           break
        else:
           print("Please enter a valid input.")
    return choice


def game():
    os.system('clr' if os.name == 'nt' else 'clear') #clears all extra terminal data in order to make it look better
    while True:
        
        computer = comp()
        choice = get_guess()
        print(f"\nPlayer chose {choice}.\nComputer chose {computer}")
        if choice == computer:
            print(f"\nBoth chose {choice}! Try again.\n")
        else: 
            if choice == "rock":
                if computer == "paper":
                    print(f"\n{computer} covers {choice}! You lose :(")
                    break
                else: 
                    print("\nRock crushes scissors! You win!")
                    break
                    
            elif choice == "paper":
                if computer == "scissors":
                    print(f"\n{computer} cuts {choice}! You lose :(") 
                    break       
                else: 
                    print("\nPaper covers rock! You win!")
                    break

            elif choice == "scissors":
                if computer == "rock":
                    print(f"\n{computer} smashes {choice}! You lose :(")
                    break
                else:                                                           
                    print("\nScissors cuts paper! You win! :)")
                    break
                    
    play_again = input("\nIf you would like to play again please type in y: \n")
    if play_again == "y":           
        game()
    else:
        print("\nThank you for playing!\n") 
        

game()