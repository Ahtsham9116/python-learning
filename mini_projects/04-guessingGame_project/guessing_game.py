#==================================

# project: Guessing Game
# Author: Muhammad Ahtsham Javed
# Language: Python
# version: 1.0

#==================================

import random

separator = '=' * 35
EASY = 10
MEDIUM = 100
HARD = 1000


class Game:
    
    def __init__(self, difficulty_level_range=MEDIUM):
        self.__difficulty_level_range = difficulty_level_range
        self.__random_number = random.randint(1, self.__difficulty_level_range)
        self.__attempts = 0
        
    def play(self):
        print("\n---------------Rules----------------")
        print(f"  1. I have selected a random number from 1 to {self.__difficulty_level_range}.")
        print("  2. Try to guess the number in as few attempts as possible.")
        
        while True:
            try:
                guess = int(input("Enter your guess: "))
                self.__attempts += 1
                
                if guess < self.__random_number:
                    print("Too low! Try again.")
                elif guess > self.__random_number:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You've guessed the number {self.__random_number} in {self.__attempts} attempts.\n")
                    break
            except ValueError:
                print("Invalid input. Please enter an integer.")
            except EOFError:
                print("\nInput stream closed. Exiting game.")
                break
            
                
    def reset(self):
        self.__random_number = random.randint(1, self.__difficulty_level_range)
        self.__attempts = 0
    
    def set_difficulty_level(self, level):
        levels = {
            "easy": EASY,
            "medium": MEDIUM,
            "hard": HARD,
        }

        if level not in levels:
            print("Invalid level. Please choose 'easy', 'medium', or 'hard'.")
            return False

        self.__difficulty_level_range = levels[level]
        self.__random_number = random.randint(1, self.__difficulty_level_range)
        self.__attempts = 0
        print(f"Difficulty set to {level.title()}.")
        return True
            
def menu():
    print(separator)
    print("    Welcome to the Guessing Game!    ")
    print(separator)
    print("1. Play Game")
    print("2. Set Difficulty Level")
    print("3. Exit")
    try:
        return input("Enter your choice (1-3): ").strip()
    except EOFError:
        print("\nInput stream closed. Exiting game.")
        return "3"

def main():
    game = Game()
    
    while True:
        choice = menu()
        
        if choice == "1":
            while True:
                game.play()
                try:
                    play_more = input("Do you want to play more (y/n):  ").strip().lower()
                except EOFError:
                    print("\nInput stream closed. Exiting game.")
                    play_more = 'n'
                if play_more == 'y':
                    game.reset()
                    continue
                print("Thank you for playing our game...")
                break
        elif choice == "2":
            level = input("Enter difficulty level (easy, medium, hard): ").strip().lower()
            game.set_difficulty_level(level)
        elif choice == "3":
            print("Thank you for playing...")
            print(separator)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
            
if __name__ == "__main__":
    main()