import random
import sys
from ascii_art import STAGES, MAX_MISTAKES

WORDS = ["python", "git", "github", "snowman", "meltdown", "hangman", "programming"]


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_header():
    """Displays the game header."""
    print("\n" + "=" * 40)
    print("||      SNOWMAN MELTDOWN      ||")
    print("=" * 40)
    print(f"Guess the word before your snowman melts!\n(Max mistakes: {MAX_MISTAKES})")
    print("=" * 40 + "\n")


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current game state."""
    print(STAGES[mistakes])

    # Word display with color coding
    display_word = []
    for letter in secret_word:
        if letter in guessed_letters:
            display_word.append(f"\033[92m{letter}\033[0m")  # Green for correct
        else:
            display_word.append("_")

    print("\nWord:    " + " ".join(display_word))
    print(f"Mistakes: \033[91m{mistakes}\033[0m/{MAX_MISTAKES}")  # Red for mistakes
    print("Guessed: " + " ".join(sorted(guessed_letters)))
    print("-" * 40)


def validate_guess(guess, guessed_letters):
    """Validates the user's guess with detailed feedback."""
    if len(guess) != 1:
        return False, "Please enter exactly ONE letter."
    if not guess.isalpha():
        return False, "Only alphabetical characters allowed."
    if guess in guessed_letters:
        return False, f"You already guessed '{guess}'."
    return True, ""


def get_guess(guessed_letters):
    """Handles user input with validation."""
    while True:
        guess = input("\nEnter your guess: ").lower()
        is_valid, message = validate_guess(guess, guessed_letters)
        if is_valid:
            return guess
        print(f"\033[91mInvalid: {message}\033[0m")  # Red error messages


def check_win(secret_word, guessed_letters):
    """Checks if all letters have been guessed."""
    return all(letter in guessed_letters for letter in secret_word)


def play_round():
    """Manages a single game round."""
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0

    display_header()

    while mistakes < MAX_MISTAKES:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess not in secret_word:
            mistakes += 1
            print(f"\n\033[91mWrong! The snowman melts a little...\033[0m")

        if check_win(secret_word, guessed_letters):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("\n\033[92mYou saved the snowman! ☃️\033[0m")
            print(f"The word was: \033[92m{secret_word}\033[0m")
            return True

    # Game over - snowman melted
    display_game_state(mistakes, secret_word, guessed_letters)
    print("\n\033[91mGame over! The snowman melted completely! 💧\033[0m")
    print(f"The word was: \033[91m{secret_word}\033[0m")
    return False


def ask_replay():
    """Asks if player wants to play again."""
    while True:
        choice = input("\nPlay again? (y/n): ").lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        print("Please enter 'y' or 'n'.")


def play_game():
    """Main game loop with replay option."""
    while True:
        play_round()
        if not ask_replay():
            print("\nThanks for playing Snowman Meltdown! ❄️")
            sys.exit()


if __name__ == "__main__":
    play_game()