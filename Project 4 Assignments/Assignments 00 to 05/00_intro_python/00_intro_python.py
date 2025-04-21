def get_integer_input(prompt):
    """Get a valid integer input from the user."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

def main():
    print("Welcome to the Sum Calculator!")
    print("-----------------------------")
    
    # Get first number
    num1 = get_integer_input("Enter the first number: ")
    
    # Get second number
    num2 = get_integer_input("Enter the second number: ")
    
    # Calculate sum
    result = num1 + num2
    
    # Display result
    print(f"\nThe sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main() 