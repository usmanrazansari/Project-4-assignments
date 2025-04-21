INCHES_PER_FOOT = 12

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

def main():
    while True:
        try:
            feet_input = input("Enter a number of feet (or 'q' to quit): ")
            
            if feet_input.lower() == 'q':
                break
                
            feet = float(feet_input)
            inches = feet_to_inches(feet)
            
            foot_word = "foot" if feet == 1 else "feet"
            inch_word = "inch" if inches == 1 else "inches"
            
            print(f"\n{feet} {foot_word} equals {inches} {inch_word}")
            print()
            
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main() 