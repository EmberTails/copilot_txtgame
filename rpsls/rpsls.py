# TODO: Develop a console-based Rock Paper Scissors Lizard Spock game in Python
# Game should be modular, allowing for easy updates or rule changes
# Implement game rules:
# - Scissors decapitate lizard
# - Scissors cuts paper
# - Paper covers rock 
# - Rock crushes lizard 
# - Lizard poisons Spock 
# - Spock smashes scissors 
# - Lizard eats paper 
# - Paper disproves Spock 
# - Spock vaporizes rock 
# - Rock crushes scissors
# Include user input for selecting options and display game results

import random
# Define global variables
# Define dictionary of game options

game_options = {
    1: "rock",
    2: "paper",
    3: "scissors",
    4: "lizard",
    5: "spock"
}

# Define dictionary of game rules
game_rules = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}

# Define dictionary of game results messages
result_messages = {
    "win": "You win!",
    "lose": "You lose!",
    "tie": "It's a tie!"
}

# Define the function to get the user input
def get_user_choice():
    print("Choose your option:")
    for key, value in game_options.items():
        print(f"{key}: {value}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if choice in game_options:
                return game_options[choice]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Define the function to get the computer's input
def get_computer_choice():
    return random.choice(list(game_options.values()))       

# Define the function to display game results
def display_result(user_choice, computer_choice):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print(result_messages["tie"])
    elif computer_choice in game_rules[user_choice]:
        print(result_messages["win"])
    else:
        print(result_messages["lose"])  


# Call to the main game function - gets user choice and computer choice
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    display_result(user_choice, computer_choice) 

# Call main function
if __name__ == "__main__":
    play_game() 
