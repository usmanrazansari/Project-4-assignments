def count_even(lst=None):
    """
    Counts the number of even numbers in a list.
    If no list is provided, prompts the user to enter integers.
    
    Args:
        lst (list, optional): List of integers to count evens from.
                             If None, prompts user for input.
    
    Returns:
        int: Number of even numbers in the list
    """
    # If no list is provided, get input from user
    if lst is None:
        lst = []
        while True:
            user_input = input("Enter an integer or press enter to stop: ")
            if user_input == "":
                break
            try:
                num = int(user_input)
                lst.append(num)
            except ValueError:
                print("Please enter a valid integer or press enter to stop.")
    
    # Count even numbers
    even_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
    
    print(f"Number of even numbers: {even_count}")
    return even_count

if __name__ == "__main__":
    count_even() 