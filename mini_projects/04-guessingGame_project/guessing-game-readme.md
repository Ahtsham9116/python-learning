# Number Guessing Game

A command-line number guessing game built with Python OOP — pick a difficulty, guess the target number, and see how few attempts it takes.

## How it works
The program picks a random number within a range you choose (Easy: 1–10, Medium: 1–100, Hard: 1–1000). After every guess it tells you whether to go higher or lower, and tracks how many attempts the round took.

## Features
- Three difficulty levels: Easy, Medium, Hard
- Attempt counter for each round
- Replay option without restarting the program
- Invalid input (non-numbers) handled without crashing
- Closed/interrupted input streams handled gracefully

## How to run
```bash
python guessing_game.py
```
Then follow the on-screen menu: play a round, change difficulty, or exit.

## Example
```
===================================
    Welcome to the Guessing Game!
===================================
1. Play Game
2. Set Difficulty Level
3. Exit
Enter your choice (1-3): 1

---------------Rules----------------
  1. I have selected a random number from 1 to 100.
  2. Try to guess the number in as few attempts as possible.
Enter your guess: 50
Too high! Try again.
Enter your guess: 25
Too low! Try again.
Enter your guess: 37
Congratulations! You've guessed the number 37 in 3 attempts.

Do you want to play more (y/n): n
Thank you for playing our game...
```

## What I learned building this
- Structuring a small program around a class instead of loose functions — bundling the game's state (target number, attempt count, difficulty) inside one object instead of passing variables around.
- Handling more than one kind of failure at once — invalid input (`ValueError`) and an interrupted input stream (`EOFError`) need different responses, not one generic catch-all.
- Using a dictionary to map difficulty names to number ranges instead of a long if/elif chain.

## Tech used
Python 3 · Object-Oriented Programming · Exception handling
