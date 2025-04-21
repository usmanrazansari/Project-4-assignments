def main():
    # Create an empty list to store values
    values = []
    
    # Continuously ask for input until empty input is received
    while True:
        value = input("Enter a value: ")
        if value == "":  # If user just presses enter
            break
        values.append(value)
    
    # Print the final list
    print("Here's the list:", values)

if __name__ == "__main__":
    main() 