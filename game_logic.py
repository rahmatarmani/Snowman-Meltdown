import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


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
    print("Word: " + " ".join(display_word))
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")


def validate_guess(guess, guessed_letters):
    """Validates the user's guess."""
    if len(guess) != 1:
        print("Please enter exactly one letter.")
        return False
    if not guess.isalpha():
        print("Please enter a letter (a-z).")
        return False
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        return False
    return True


def play_game():
    """Main game loop for Snowman Meltdown."""
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("\nWelcome to Snowman Meltdown!")
    print(f"Guess the word before the snowman melts! (Max mistakes: {max_mistakes})")

    while mistakes < max_mistakes:
        # Display current game state
        display_game_state(mistakes, secret_word, guessed_letters)

        # Get and validate user input
        while True:
            guess = input("\nGuess a letter: ").lower()
            if validate_guess(guess, guessed_letters):
                break

        guessed_letters.add(guess)

        # Check if letter is in the word
        if guess in secret_word:
            print(f"\nCorrect! '{guess}' is in the word.")
        else:
            print(f"\nSorry, '{guess}' is not in the word.")
            mistakes += 1

        # Check if all letters have been guessed
        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("\nCongratulations! You saved the snowman!")
            print(f"The word was: {secret_word}")
            return

    # If we get here, the player lost
    display_game_state(mistakes, secret_word, guessed_letters)
    print("\nGame over! The snowman melted completely.")
    print(f"The secret word was: {secret_word}")


if __name__ == "__main__":
    play_game()