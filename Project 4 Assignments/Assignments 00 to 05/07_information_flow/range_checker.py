def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    
    Args:
        n: The number to check
        low: The lower bound of the range
        high: The upper bound of the range
        
    Returns:
        bool: True if n is between low and high (inclusive), False otherwise
    """
    return low <= n <= high

def main():
    # Example usage
    print(in_range(5, 1, 10))  # Should print True
    print(in_range(1, 1, 10))  # Should print True
    print(in_range(10, 1, 10))  # Should print True
    print(in_range(0, 1, 10))  # Should print False
    print(in_range(11, 1, 10))  # Should print False

if __name__ == "__main__":
    main() 