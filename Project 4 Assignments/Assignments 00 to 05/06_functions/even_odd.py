def print_even_odd():
    """
    Prints numbers from 10 to 19, labeling each as even or odd.
    """
    for num in range(10, 20):
        if num % 2 == 0:
            print(f"{num} even", end=' ')
        else:
            print(f"{num} odd", end=' ')
    print()  # Print a newline at the end

def main():
    print_even_odd()

if __name__ == "__main__":
    main() 