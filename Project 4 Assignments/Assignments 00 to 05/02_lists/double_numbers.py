def double_numbers(numbers):
    """
    Double each element in a list of numbers.
    
    Args:
        numbers (list): A list of numbers to be doubled
        
    Returns:
        list: A new list with each element doubled
    """
    return [num * 2 for num in numbers]

# Example usage
if __name__ == "__main__":
    # Test cases
    test_list1 = [1, 2, 3, 4]
    test_list2 = [10, 20, 30]
    test_list3 = [-1, 0, 1]
    
    print(f"Original list: {test_list1}")
    print(f"Doubled list: {double_numbers(test_list1)}")
    print()
    
    print(f"Original list: {test_list2}")
    print(f"Doubled list: {double_numbers(test_list2)}")
    print()
    
    print(f"Original list: {test_list3}")
    print(f"Doubled list: {double_numbers(test_list3)}") 