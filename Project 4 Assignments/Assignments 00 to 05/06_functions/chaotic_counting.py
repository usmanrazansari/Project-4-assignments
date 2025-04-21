import random

DONE_LIKELIHOOD = 0.2  # 20% chance of stopping at each number

def done():
    """Returns True with probability DONE_LIKELIHOOD."""
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    """
    Counts from 1 to 10, but may stop early if done() returns True.
    Prints each number as it counts.
    """
    for i in range(1, 11):
        if done():
            return
        print(i, end=' ')
    print()  # Print a newline after counting

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.", end=' ')
    chaotic_counting()
    print("I'm done.")

if __name__ == "__main__":
    main() 