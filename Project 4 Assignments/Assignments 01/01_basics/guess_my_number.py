import random

# Generate a random number between 0 and 99
secret_number = random.randint(0, 99)

# Get initial guess from user
guess = int(input("I am thinking of a number between 0 and 99... Enter a guess: "))

# Keep asking for guesses until the correct number is found
while guess != secret_number:
    if guess > secret_number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
    
    guess = int(input("Enter a new number: "))

# When the loop ends, the guess is correct
print(f"Congrats! The number was: {secret_number}") 