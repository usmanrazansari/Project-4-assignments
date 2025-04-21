def print_ones_digit(num):
    """
    Prints the ones digit of the given number.
    
    Args:
        num (int): The number to get the ones digit from
    """
    ones_digit = abs(num) % 10  # Use abs() to handle negative numbers
    print(f"The ones digit is {ones_digit}")

def main():
    try:
        num = int(input("Enter a number: "))
        print_ones_digit(num)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main() 