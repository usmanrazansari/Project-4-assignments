def make_sentence(word, part_of_speech):
    """
    Generates a sentence using the given word based on its part of speech.
    
    Args:
        word (str): The word to use in the sentence
        part_of_speech (int): 0 for noun, 1 for verb, 2 for adjective
    """
    if part_of_speech == 0:  # noun
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:  # verb
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:  # adjective
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid part of speech. Please use 0 for noun, 1 for verb, or 2 for adjective.")

def main():
    word = input("Please type a noun, verb, or adjective: ")
    try:
        part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
        make_sentence(word, part_of_speech)
    except ValueError:
        print("Please enter a valid number (0, 1, or 2) for the part of speech.")

if __name__ == "__main__":
    main() 