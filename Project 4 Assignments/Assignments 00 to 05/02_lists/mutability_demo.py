def add_three_copies(lst, data):
    """
    Add three copies of the data to the list.
    This function modifies the list in place without returning anything.
    
    Args:
        lst (list): The list to modify
        data: The data to add three copies of
    """
    lst.append(data)
    lst.append(data)
    lst.append(data)

def main():
    # Get input from user
    message = input("Enter a message to copy: ")
    
    # Create an empty list
    my_list = []
    
    # Show the list before modification
    print("\nList before:", my_list)
    
    # Call the function to modify the list
    add_three_copies(my_list, message)
    
    # Show the list after modification
    print("List after:", my_list)

if __name__ == "__main__":
    main() 