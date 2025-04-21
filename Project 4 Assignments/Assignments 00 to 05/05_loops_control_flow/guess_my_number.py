import random

def play_guessing_game():
    # Generate a random number between 0 and 99 (inclusive)
    secret_number = random.randint(0, 99)
    attempts = 0
    
    print("I am thinking of a number between 0 and 99...")
    
    while True:
        try:
            # Get user's guess
            guess = int(input("Enter a guess: "))
            attempts += 1
            
            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congrats! The number was: {secret_number}")
                break
            # Give feedback if the guess is too high or too low
            elif guess > secret_number:
                print("Your guess is too high")
            else:
                print("Your guess is too low")
                
        except ValueError:
            print("Please enter a valid number!")

# Start the game
if __name__ == "__main__":
    play_guessing_game() 