def count_numbers():
    number_counts = {}
    
    print("Enter numbers (press Enter without typing anything to finish):")
    
    while True:
        user_input = input("Enter a number: ")
        
        if user_input == "":
            break
            
        try:
            number = int(user_input)
            
            if number in number_counts:
                number_counts[number] += 1
            else:
                number_counts[number] = 1
                
        except ValueError:
            print("Please enter a valid number.")
    
    print("\nResults:")
    for number, count in sorted(number_counts.items()):
        print(f"{number} appears {count} times.")

if __name__ == "__main__":
    count_numbers() 