"""
Game of Pig - ICS3U Unit 2 Project
Author: Ismail Kaan Yucel
Date: 2026

Description:
This program simulates a Human vs Computer version of the Game of Pig.
The user can choose between manual (r/h) mode or automatic mode.

# Player chooses to roll or hold
# Computer uses strategy to stop at 20
# Game loop continues until a player reaches 100
"""

import random
import time


# Roll a die
def roll_die():
    return random.randint(1, 6)


# Player turn (manual mode)
def player_turn_manual():
    turn_total = 0
    print("\n--- Your Turn (Manual) ---")

    while True:
        choice = input("Roll or Hold? (r/h): ").lower().strip()

        if choice not in ['r', 'h']:
            print("Please enter only 'r' or 'h'")
            continue

        if choice == 'r':
            roll = roll_die()
            print(f"You rolled: {roll}")

            if roll == 1:
                print("You rolled a 1! Turn over.\n")
                return 0
            else:
                turn_total += roll
                print(f"Turn total: {turn_total}")

        elif choice == 'h':
            print(f"You hold. Added {turn_total} to your score.\n")
            return turn_total


# Player turn (auto mode)
def player_turn_auto():
    turn_total = 0
    print("\n--- Your Turn (Auto Mode) ---")
    input("Press ENTER to start rolling...")

    while True:
        roll = roll_die()
        print(f"You rolled: {roll}")
        time.sleep(1)

        if roll == 1:
            print("You rolled a 1! Turn over.\n")
            return 0
        else:
            turn_total += roll
            print(f"Turn total: {turn_total}")
            time.sleep(1)


# Computer turn
def computer_turn(computer_score):
    turn_total = 0
    print("\n--- Computer Turn ---")

    while turn_total < 20 and (computer_score + turn_total) < 100:
        roll = roll_die()
        print(f"Computer rolled: {roll}")
        time.sleep(1)

        if roll == 1:
            print("Computer rolled a 1! Turn over.\n")
            return 0
        else:
            turn_total += roll

    print(f"Computer holds with {turn_total}\n")
    return turn_total


# Check winner
def check_winner(player_score, computer_score):
    if player_score >= 100:
        print("You win!")
        return True
    elif computer_score >= 100:
        print("Computer wins!")
        return True
    return False


# Choose game mode
def choose_mode():
    while True:
        mode = input("Choose mode: (m)anual or (a)uto: ").lower().strip()
        if mode in ['m', 'a']:
            return mode
        print("Please enter 'm' or 'a'")


# Main game loop
def game():
    print("🎲 Welcome to the Game of Pig!\n")

    while True:
        player_score = 0
        computer_score = 0

        mode = choose_mode()

        while True:
            print("\n==========================")
            print(f"Scores → You: {player_score} | Computer: {computer_score}")
            print("==========================")

            # Player turn
            if mode == 'm':
                player_score += player_turn_manual()
            else:
                player_score += player_turn_auto()

            if check_winner(player_score, computer_score):
                break

            # Computer turn
            computer_score += computer_turn(computer_score)

            if check_winner(player_score, computer_score):
                break

        # Replay
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != 'y':
            print("Thanks for playing!")
            break


# Run game
game()