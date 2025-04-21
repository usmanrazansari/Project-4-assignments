# Define the age at which someone is considered an adult in the US
ADULT_AGE = 18

def is_adult(age):
    """
    Check if the given age classifies someone as an adult.
    
    Args:
        age: The age to check
        
    Returns:
        bool: True if the person is an adult, False otherwise
    """
    return age >= ADULT_AGE

def main():
    # Get age input from the user
    age = int(input("How old is this person?: "))
    
    # Print the result of checking if they're an adult
    print(is_adult(age))

if __name__ == "__main__":
    main()
