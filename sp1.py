import random

def play_game():
    print("Welcome to Stone, Paper, Scissors!")
    print("-----------------------------------")
    
    # Define the valid choices
    choices = ['stone', 'paper', 'scissors']
    
    # Initialize scores
    user_score = 0
    computer_score = 0

    while True:
        # Get user's choice
        user_choice = input("\nEnter your choice (stone, paper, scissors) or 'quit' to exit: ").lower()
        
        # Check if the user wants to quit
        if user_choice == 'quit':
            print("\n--- Final Score ---")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break
            
        # Validate user input
        if user_choice not in choices:
            print("Invalid input. Please type 'stone', 'paper', or 'scissors'.")
            continue
            
        # Get computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'stone' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'stone') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
            
        # Display current score
        print(f"Current Score -> You: {user_score} | Computer: {computer_score}")

# Run the game
if __name__ == "__main__":
    play_game()
