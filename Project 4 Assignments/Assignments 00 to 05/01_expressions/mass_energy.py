SPEED_OF_LIGHT = 299792458

def calculate_energy(mass):
    return mass * SPEED_OF_LIGHT**2

def main():
    while True:
        try:
            mass_input = input("Enter kilos of mass (or 'q' to quit): ")
            
            if mass_input.lower() == 'q':
                break
                
            mass = float(mass_input)
            
            print("\ne = m * C^2...")
            print(f"\nm = {mass} kg")
            print(f"C = {SPEED_OF_LIGHT} m/s")
            
            energy = calculate_energy(mass)
            print(f"\n{energy} joules of energy!")
            print()
            
        except ValueError:
            print("Please enter a valid number for mass.")
            
if __name__ == "__main__":
    main() 