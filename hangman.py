import random


def play_game():
    # 1. Predefined list of 5 words
    words = ["python", "coding", "software", "keyboard", "challenge"]

    # 2. Select a secret word at random
    secret_word = random.choice(words)

    # 3. Track game state using lists and variables
    guessed_letters = []
    max_incorrect_guesses = 6
    incorrect_guesses = 0

    print("=" * 40)
    print("          WELCOME TO HANGMAN")
    print("=" * 40)
    print(f"Guess the secret word! You have {max_incorrect_guesses} incorrect guesses allowed.\n")

    # 4. Main game loop
    while incorrect_guesses < max_incorrect_guesses:
        # Build the current displayed word with blanks for unguessed letters
        display_word = []
        for letter in secret_word:
            if letter in guessed_letters:
                display_word.append(letter)
            else:
                display_word.append("_")

        # Show current progress and remaining attempts
        print(f"Word: {' '.join(display_word)}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print(f"Remaining incorrect guesses: {max_incorrect_guesses - incorrect_guesses}")

        # Check win condition: no underscores remaining
        if "_" not in display_word:
            print("\n Congratulations! You guessed the word correctly!")
            print(f"The secret word was: {secret_word}")
            return

        # 5. Receive and validate player input
        guess = input("\nEnter a letter: ").strip().lower()

        # Validate input: single alphabetical character
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single alphabetical letter.\n")
            continue

        # Check for repeated guesses
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.\n")
            continue

        guessed_letters.append(guess)

        # 6. Check if the guess is in the secret word
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"Incorrect! '{guess}' is not in the word.\n")

    # If the while loop ends without winning, the player lost
    print("=" * 40)
    print(" Game Over! You ran out of guesses.")
    print(f"The secret word was: {secret_word}")
    print("=" * 40)


if __name__ == "__main__":
    play_game()
