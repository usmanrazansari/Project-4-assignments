def get_last_element(lst):
    """
    Print the last element of the list.
    
    Args:
        lst (list): A non-empty list
    """
    print(lst[-1])

def main():
    # Create an empty list
    my_list = []
    
    # Get the number of elements from the user
    num_elements = int(input("How many elements in your list? "))
    
    # Get each element from the user
    for i in range(num_elements):
        element = input(f"Enter element {i + 1}: ")
        my_list.append(element)
    
    # Print the last element
    print("\nThe last element is:")
    get_last_element(my_list)

if __name__ == "__main__":
    main() 