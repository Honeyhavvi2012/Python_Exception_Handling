import random

while True:
    user_action = input("Enter a choice (rock, paper, scissors:)")
    possible_action = ["rock","paper","scissors"]
    computer_action = random.choice(possible_action)
    print(f"\nYou choice {user_action}, computer chose {computer_action}.\n")
    if user_action == computer_action:
        print(f"Both players selested{user_action}. It's tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper cover rock ! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper cover rock ! You win!")
        else:
            print("Scissirs cuts paper!You lose.")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Scissirs cuts paper!You win!")
        else:
            print("Rock smashes scissors! You lose")
    play_again = input("Play again? (y/n):")
    if play_again != "y":
        break