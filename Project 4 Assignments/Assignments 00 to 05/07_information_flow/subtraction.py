def subtract_seven(num):
    """
    Subtracts 7 from the given number.
    
    Args:
        num: The number to subtract 7 from
        
    Returns:
        int: The result of subtracting 7 from num
    """
    return num - 7

def main():
    # Get number input from the user
    number = int(input("Enter a number to subtract 7 from: "))
    
    # Calculate and print the result
    result = subtract_seven(number)
    print(f"{number} - 7 = {result}")

if __name__ == "__main__":
    main() 