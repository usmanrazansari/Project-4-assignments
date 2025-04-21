MAX_LENGTH = 3

def shorten(lst):
    """
    Remove elements from the end of the list until it is MAX_LENGTH items long.
    Print each removed item.
    
    Args:
        lst (list): The list to shorten
    """
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(f"Removed: {removed_item}")

def main():
    # Get the number of elements from the user
    num_elements = int(input("How many elements in your list? "))
    
    # Create an empty list
    my_list = []
    
    # Get each element from the user
    for i in range(num_elements):
        element = input(f"Enter element {i + 1}: ")
        my_list.append(element)
    
    # Print the original list
    print("\nOriginal list:", my_list)
    
    # Shorten the list
    shorten(my_list)
    
    # Print the final list
    print("Final list:", my_list)

if __name__ == "__main__":
    main() 