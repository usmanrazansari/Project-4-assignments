def fahrenheit_to_celsius():
    # Get input from user
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert to Celsius using the formula: C = (F - 32) * 5/9
    celsius = (fahrenheit - 32) * 5/9
    
    # Print the result with 2 decimal places
    print(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C")

if __name__ == "__main__":
    fahrenheit_to_celsius() 