def num_in_stock(fruit):
    """
    Returns the number of a specific fruit in Sophia's inventory.
    
    Args:
        fruit: The name of the fruit to check
        
    Returns:
        int: The number of that fruit in stock, or 0 if not in stock
    """
    # Sophia's fruit inventory
    inventory = {
        "apple": 500,
        "banana": 750,
        "orange": 300,
        "pear": 1000,
        "grape": 200
    }
    return inventory.get(fruit.lower(), 0)

def main():
    # Get fruit input from the user
    fruit = input("Enter a fruit: ")
    
    # Check inventory
    quantity = num_in_stock(fruit)
    
    if quantity > 0:
        print("This fruit is in stock! Here is how many:")
        print(quantity)
    else:
        print("This fruit is not in stock.")

if __name__ == "__main__":
    main() 