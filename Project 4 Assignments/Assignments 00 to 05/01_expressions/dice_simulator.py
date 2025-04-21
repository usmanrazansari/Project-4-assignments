import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total: {total}")

def main():
    while True:
        input("Press Enter to roll the dice (or 'q' to quit): ")
        roll_dice()
        print()

if __name__ == "__main__":
    main() 