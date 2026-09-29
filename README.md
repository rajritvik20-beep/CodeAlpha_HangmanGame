# Task 1: Hangman Game

A simple, text-based Hangman game implemented in Python where players guess a word one letter at a time.

## Features
- **Predefined Word List**: Selects from 5 predefined words.
- **Limited Attempts**: Players are allowed up to 6 incorrect guesses.
- **Input Validation**: Ensures guesses are single alphabetical characters and warns against duplicate guesses.
- **Pure Console Interface**: Simple text-based I/O without any external dependencies.

## Concepts Used
- `random`: For randomly choosing words.
- `while` loop: For driving the main gameplay loop.
- `if-else` statements: For condition checking, input validation, and win/loss states.
- `strings` & `lists`: For tracking hidden words and guessed letters.

## Getting Started

### Prerequisites
- Python 3.x installed.

### Running the Game
Open a terminal in this directory and run:
```bash
python hangman.py
```
