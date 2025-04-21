def access_element(lst, index):
    """Access an element at the specified index."""
    if 0 <= index < len(lst):
        return lst[index]
    return "Index out of range!"

def modify_element(lst, index, new_value):
    """Modify an element at the specified index."""
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"Element at index {index} updated to {new_value}"
    return "Index out of range!"

def slice_list(lst, start, end):
    """Return a slice of the list from start to end."""
    if 0 <= start < len(lst) and 0 <= end <= len(lst):
        return lst[start:end]
    return "Invalid start or end index!"

def main():
    # Initialize a list with 5 different elements
    my_list = [10, "hello", 3.14, True, "world"]
    
    print("Welcome to the List Manipulation Game!")
    print(f"Current list: {my_list}")
    
    while True:
        print("\nChoose an operation:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice list")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            try:
                index = int(input("Enter the index: "))
                result = access_element(my_list, index)
                print(f"Element at index {index}: {result}")
            except ValueError:
                print("Please enter a valid integer index!")
        
        elif choice == "2":
            try:
                index = int(input("Enter the index: "))
                new_value = input("Enter the new value: ")
                result = modify_element(my_list, index, new_value)
                print(result)
                print(f"Updated list: {my_list}")
            except ValueError:
                print("Please enter a valid integer index!")
        
        elif choice == "3":
            try:
                start = int(input("Enter the start index: "))
                end = int(input("Enter the end index: "))
                result = slice_list(my_list, start, end)
                print(f"Sliced list: {result}")
            except ValueError:
                print("Please enter valid integer indices!")
        
        elif choice == "4":
            print("Thanks for playing!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main() 