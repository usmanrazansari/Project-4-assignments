def calculate_fruit_cost():
    fruit_prices = {
        "apple": 2.5,
        "durian": 15.0,
        "jackfruit": 10.0,
        "kiwi": 1.5,
        "rambutan": 3.0,
        "mango": 4.0
    }
    
    total_cost = 0.0
    
    for fruit in fruit_prices:
        while True:
            try:
                quantity = int(input(f"How many ({fruit}) do you want?: "))
                if quantity >= 0:
                    total_cost += quantity * fruit_prices[fruit]
                    break
                else:
                    print("Please enter a non-negative number.")
            except ValueError:
                print("Please enter a valid number.")
    
    print(f"\nYour total is ${total_cost:.1f}")

if __name__ == "__main__":
    calculate_fruit_cost() 