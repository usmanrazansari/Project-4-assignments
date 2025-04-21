from math import sqrt

def calculate_hypotenuse(side_a, side_b):
    return sqrt(side_a**2 + side_b**2)

def main():
    while True:
        try:
            side_ab = float(input("Enter the length of AB: "))
            side_ac = float(input("\nEnter the length of AC: "))
            
            if side_ab <= 0 or side_ac <= 0:
                print("Please enter positive numbers for the sides.")
                continue
                
            hypotenuse = calculate_hypotenuse(side_ab, side_ac)
            print(f"\nThe length of BC (the hypotenuse) is: {hypotenuse}")
            break
            
        except ValueError:
            print("Please enter valid numbers.")

if __name__ == "__main__":
    main() 