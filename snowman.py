import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    ( : ) 
    """,
    # Stage 1: Bottom part starts melting
    """
     ___  
    /___\\ 
    (o o) 
    ( : ) 
    """,
    # Stage 2: Only the head remains
    """
     ___  
    /___\\ 
    (o o) 
    """,
    # Stage 3: Snowman completely melted
    """
     ___  
    /___\\ 
    """
]


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current game state including snowman and word progress."""
    # Show the appropriate stage based on mistakes
    print(STAGES[mistakes])

    # Display the word with underscores for unguessed letters
    display_word = []
    for letter in secret_word:
        if letter in guessed_letters:
            display_word.append(letter)
        else:
            display_word.append("_")
    print(" ".join(display_word))
    print()


def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")
    print(f"Guess the word before the snowman melts! (Max mistakes: {max_mistakes})")

    while mistakes < max_mistakes:
        # Display current game state
        display_game_state(mistakes, secret_word, guessed_letters)

        # Get user input
        guess = input("Guess a letter: ").lower()

        # Check if letter is in the word
        if guess in secret_word:
            print(f"Correct! '{guess}' is in the word.")
            guessed_letters.add(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            mistakes += 1

        # Check if all letters have been guessed
        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You won!")
            print(f"The word was: {secret_word}")
            return

    # If we get here, the player lost
    display_game_state(mistakes, secret_word, guessed_letters)
    print("\nGame over! The snowman melted completely.")
    print(f"The secret word was: {secret_word}")


if __name__ == "__main__":
    play_game()