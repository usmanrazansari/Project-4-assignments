def print_multiple(message, repeats):
    """
    Prints a message multiple times.
    
    Args:
        message (str): The message to print
        repeats (int): Number of times to print the message
    """
    for _ in range(repeats):
        print(message, end=' ')
    print()  # Print a newline at the end

def main():
    message = input("Please type a message: ")
    try:
        repeats = int(input("Enter a number of times to repeat your message: "))
        print_multiple(message, repeats)
    except ValueError:
        print("Please enter a valid integer for the number of repeats.")

if __name__ == "__main__":
    main() 