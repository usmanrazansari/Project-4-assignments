import random

# Constants
NUM_ROUNDS = 5

def get_valid_input():
    while True:
        choice = input("Do you think your number is higher or lower than the computer's?: ").lower()
        if choice in ["higher", "lower"]:
            return choice
        print("Please enter either higher or lower: ", end="")

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0
    
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"\nRound {round_num}")
        
        # Generate random numbers
        computer_number = random.randint(1, 100)
        player_number = random.randint(1, 100)
        
        print(f"Your number is {player_number}")
        
        # Get valid user input
        user_choice = get_valid_input()
        
        # Determine if the guess was correct
        is_higher = player_number > computer_number
        is_lower = player_number < computer_number
        
        # Check if the guess was correct
        if (user_choice == "higher" and is_higher) or (user_choice == "lower" and is_lower):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}")
    
    print("\nThanks for playing!")
    
    # Print conditional ending message
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main() 