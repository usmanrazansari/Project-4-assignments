def check_affirmation():
    affirmation = "I am capable of doing anything I put my mind to."
    
    while True:
        print(f"Please type the following affirmation: {affirmation}")
        user_input = input()
        
        if user_input == affirmation:
            print("That's right! :)")
            break
        else:
            print("Hmmm That was not the affirmation.")

if __name__ == "__main__":
    check_affirmation() 