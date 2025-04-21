import random

total_rolls = 0

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    global total_rolls
    total_rolls += 1
    
    print(f"Roll {total_rolls}:")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total: {die1 + die2}\n")
    
    return die1, die2

def main():
    for _ in range(3):
        roll_dice()
    
    print(f"Total number of rolls: {total_rolls}")

if __name__ == "__main__":
    main()