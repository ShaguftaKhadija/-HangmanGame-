
import random


def display_hangman(wrong_guesses):
    stages = [
        """
          +---+
          |   |
              |
              |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        =========
        """
    ]

    print(stages[wrong_guesses])


def play_game():
    words = {
        "python": "A popular programming language",
        "planet": "A celestial body that orbits a star",
        "laptop": "A portable computer",
        "garden": "A place where plants and flowers grow",
        "puzzle": "A game that tests your thinking skills",
        "school": "A place where students learn",
        "rocket": "A vehicle used to travel into space",
        "coding": "The process of writing computer instructions",
        "forest": "A large area covered with trees",
        "camera": "A device used to take photographs"
    }

    word = random.choice(list(words.keys()))
    hint = words[word]

    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 5

    print("\n" + "=" * 42)
    print("          THE HANGMAN CHALLENGE")
    print("=" * 42)

    print("\nYour mission: Guess the hidden word!")
    print("You have 6 lives. Use them wisely.")
    print(f"\nHINT: {hint}")

    while wrong_guesses < max_wrong_guesses + 1:

        display_hangman(wrong_guesses)

        displayed_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in word
        )

        print("Word:          ", displayed_word)
        print("Guessed letters:", ", ".join(guessed_letters) or "None")
        print("Lives remaining:", max_wrong_guesses + 1 - wrong_guesses)

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word!")
            print("The hidden word was:", word)
            return True

        guess = input("\nEnter one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct! That letter is in the word.")
        else:
            wrong_guesses += 1
            print("Oops! That letter is not in the word.")

    display_hangman(wrong_guesses)

    print("\nGAME OVER!")
    print("The hidden word was:", word)

    return False


def main():
    games_played = 0
    games_won = 0

    while True:
        print("\nWelcome to Hangman!")
        print("1. Start Game")
        print("2. View Score")
        print("3. Exit")

        choice = input("\nChoose an option (1-3): ").strip()

        if choice == "1":
            games_played += 1

            if play_game():
                games_won += 1

        elif choice == "2":
            print("\n========== YOUR SCORE ==========")
            print("Games played:", games_played)
            print("Games won:   ", games_won)
            print("Games lost:  ", games_played - games_won)

            if games_played > 0:
                percentage = games_won / games_played * 100
                print(f"Win rate:     {percentage:.1f}%")
            else:
                print("Play a game to see your win rate!")

            print("================================")

        elif choice == "3":
            print("\nThanks for playing Hangman!")
            print("Keep learning and keep coding. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
