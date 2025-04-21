def print_divisors(num):
    """
    Prints all divisors of the given number.
    
    Args:
        num (int): The number to find divisors for
    """
    print(f"Here are the divisors of {num}", end=' ')
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=' ')
    print()  # Print a newline at the end

def main():
    try:
        num = int(input("Enter a number: "))
        print_divisors(num)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main() 