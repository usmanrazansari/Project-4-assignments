def greet(name):
    """
    Print a greeting for the given name.
    
    Args:
        name: The name to greet
    """
    print(f"Greetings {name}!")

def main():
    # Get the user's name and greet them
    name = input("What's your name? ")
    greet(name)

if __name__ == "__main__":
    main() 