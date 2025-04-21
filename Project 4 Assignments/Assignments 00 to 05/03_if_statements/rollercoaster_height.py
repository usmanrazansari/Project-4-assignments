# Rollercoaster height checker
MIN_HEIGHT = 50

def check_height():
    height = input("How tall are you? ")
    if not height:
        return False
    
    height = int(height)
    if height >= MIN_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")
    return True

# Main loop
print("Welcome to the rollercoaster height checker!")
print("(Press Enter without typing anything to exit)")
while check_height():
    pass  # Keep running until user enters nothing 