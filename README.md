# 🎮 Hangman Game — Python Edition

### Guess the Word. Save Your Lives. Win the Challenge!

A fun, interactive, command-line Hangman game developed using Python. Challenge yourself to guess hidden words with the help of hints, track your score, and see how many rounds you can win!

This project was developed as part of my **Python Programming Internship at CodeAlpha** to practise Python fundamentals through a hands-on application.

---

## ✨ Features

- 🎯 **Random Word Selection** — A different word is selected randomly for each round.
- 💡 **Helpful Hints** — Get a clue about the hidden word before guessing.
- ❤️ **Limited Lives** — You have six chances to guess incorrectly before the game ends.
- 🔤 **Interactive Guessing** — Enter one letter at a time to uncover the hidden word.
- 🎨 **ASCII Hangman Art** — Watch the hangman drawing change as incorrect guesses increase.
- 🛡️ **Input Validation** — Handles invalid inputs and prevents repeated guesses from counting twice.
- 🏆 **Score Tracking** — View games played, games won, games lost, and your win percentage.
- 🔄 **Replay Support** — Start multiple rounds without restarting the program.
- 📋 **Menu-Based Interface** — Start a game, view your score, or exit through a simple menu.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| `random` module | Randomly selects the hidden word |
| Functions | Organizes the program into reusable components |
| Lists and Dictionaries | Stores words, hints, and guessed letters |
| Conditional Statements | Controls game logic |
| Loops | Runs the game and menu |
| String Methods | Processes user input |

**Additional installations:** None required. The project uses Python's built-in modules.

---

## 📂 Project Structure

```text
CodeAlpha_HangmanGame/
│
├── hangman.py     # Main game source code
└── README.md      # Project documentation
```

---

## ⚙️ Installation and Setup

Follow these steps to run the game locally.

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Check your installation using:

```bash
python --version
```

On Windows, you can also use:

```bash
py --version
```

### Step 2: Clone the Repository

Replace the placeholder with your actual GitHub repository URL.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 3: Open the Project Folder

```bash
cd CodeAlpha_HangmanGame
```

If your folder has a different name, use that name instead.

### Step 4: Run the Game

Execute the following command:

```bash
python hangman.py
```

On Windows, you can alternatively run:

```bash
py hangman.py
```

That's it! Your Hangman game is ready to play.

---

## 🎲 How to Play

1. Launch the program.
2. Select **Start Game** from the main menu.
3. Read the hint to understand the hidden word.
4. Enter one alphabet letter at a time.
5. Correct guesses reveal letters in the word.
6. Incorrect guesses reduce your remaining lives.
7. Guess the complete word before running out of lives to win.
8. Select **View Score** to check your performance.
9. Start another round or exit whenever you want.

### 🎮 Available Menu Options

| Option | Action |
|---|---|
| `1` | Start a new game |
| `2` | View your score |
| `3` | Exit the game |

---

## 💻 Example Gameplay

```text
Welcome to Hangman!
1. Start Game
2. View Score
3. Exit

Choose an option (1-3): 1

==========================================
          THE HANGMAN CHALLENGE
==========================================

Your mission: Guess the hidden word!
You have 6 lives. Use them wisely.

HINT: A popular programming language

Word:           _ _ _ _ _ _
Guessed letters: None
Lives remaining: 6

Enter one letter: p

Correct! That letter is in the word.

Word:           p _ _ _ _ _
Guessed letters: p
Lives remaining: 6
```

*Note: This is an illustrative example. The actual word, hint, and displayed letters depend on the random selection and the player's guesses.*

---

## 🧠 Python Concepts Practised

This project provides practical experience with:

- **Functions:** Dividing the program into manageable sections.
- **Loops:** Repeating gameplay until a round or the program ends.
- **Conditional Statements:** Checking guesses and controlling game outcomes.
- **Lists:** Tracking guessed letters.
- **Dictionaries:** Associating words with their hints.
- **Randomization:** Selecting words randomly.
- **String Manipulation:** Processing letter inputs.
- **Input Validation:** Handling incorrect or repeated inputs.
- **Basic Arithmetic:** Calculating the player's win percentage.

---

## 🚀 Future Enhancements

Possible improvements for future versions include:

- 🎚️ Multiple difficulty levels.
- 📚 Larger word collections by category.
- ⏱️ A timed challenge mode.
- 💾 Saving scores between sessions.
- 🖥️ A graphical interface using Tkinter.
- 🌐 A browser-based version of the game.

These are planned ideas, not features currently implemented in this version.

---

## 🎯 Project Objective

The objective of this project is to strengthen Python programming skills by building a simple yet engaging word-guessing game.

It demonstrates how core programming concepts can be combined to create an interactive application with game logic, input validation, and score tracking.

---

## 👩‍💻 Developed By

**Shagufta Khadija**

B.Tech — Data Science

**Internship:** Python Programming Internship at CodeAlpha  
**Project:** Hangman Game

---

## 🙌 Acknowledgement

I developed this project as part of my CodeAlpha Python Programming Internship to gain hands-on experience with Python and improve my problem-solving skills.

---

⭐ If you find this project interesting, consider giving the repository a star!

**Made with Python and a love for learning.** 🐍
