def main():
    while True:
        try:
            dividend = int(input("Please enter an integer to be divided: "))
            divisor = int(input("\nPlease enter an integer to divide by: "))
            
            if divisor == 0:
                print("\nError: Cannot divide by zero. Please try again.")
                continue
                
            quotient = dividend // divisor
            remainder = dividend % divisor
            
            print(f"\nThe result of this division is {quotient} with a remainder of {remainder}")
            break
            
        except ValueError:
            print("\nPlease enter valid integers.")

if __name__ == "__main__":
    main() 