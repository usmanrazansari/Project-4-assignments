def get_user_data():
    """
    Collects user registration data including first name, last name, and email address.
    
    Returns:
        tuple: A tuple containing (first_name, last_name, email_address)
    """
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email_address = input("What is your email address?: ")
    
    return first_name, last_name, email_address

def main():
    # Get user data
    user_data = get_user_data()
    
    # Print the collected data
    print("Received the following user data:", user_data)

if __name__ == "__main__":
    main() 