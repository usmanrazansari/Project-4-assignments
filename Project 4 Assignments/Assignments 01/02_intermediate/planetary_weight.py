# Constants for planetary gravity (as percentage of Earth's gravity)
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.360
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.140

# Get user input
earth_weight = float(input("Enter a weight on Earth: "))
planet = input("Enter a planet: ")

# Calculate weight based on planet
if planet == "Mercury":
    planet_weight = earth_weight * MERCURY_GRAVITY
elif planet == "Venus":
    planet_weight = earth_weight * VENUS_GRAVITY
elif planet == "Mars":
    planet_weight = earth_weight * MARS_GRAVITY
elif planet == "Jupiter":
    planet_weight = earth_weight * JUPITER_GRAVITY
elif planet == "Saturn":
    planet_weight = earth_weight * SATURN_GRAVITY
elif planet == "Uranus":
    planet_weight = earth_weight * URANUS_GRAVITY
elif planet == "Neptune":
    planet_weight = earth_weight * NEPTUNE_GRAVITY

# Print the result rounded to 2 decimal places
print(f"The equivalent weight on {planet}: {round(planet_weight, 2)}") 