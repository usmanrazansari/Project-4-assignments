def generate_fibonacci():
    # Define the maximum value as a constant
    MAX_VALUE = 10000
    
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    # Print the first number (Fib(0))
    print(a, end=' ')
    
    # Generate and print Fibonacci numbers until we reach the maximum value
    while b < MAX_VALUE:
        print(b, end=' ')
        # Calculate the next Fibonacci number
        a, b = b, a + b

if __name__ == "__main__":
    generate_fibonacci() 