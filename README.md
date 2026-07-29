# Game-of-Pig

This project is a Python implementation of the classic **Game of Pig**, created as part of the **ICS3U Computer Science Unit 2 Project**. The objective of this assignment was not only to create a fully functional game, but also to demonstrate an understanding of modular programming, problem solving, functions, loops, conditional statements, and the software development process.

The game allows a human player to compete against a computer-controlled opponent. During each turn, players roll a six-sided die to accumulate points. Choosing to continue rolling increases the potential score for the turn, but rolling a **1** immediately ends the turn and all points earned during that round are lost. The first player to reach **100 points** wins the game.

<br>
<br>

While developing this project, I focused on writing code that is easy to understand, reusable and organized into separate functions. Rather than placing all of the logic inside a single block of code, every major part of the game was divided into its own function. This approach makes the program easier to read, debug and maintain.

The project also demonstrates the software development cycle by following the stages of planning, implementation, testing, debugging and final improvements.

<br>

## Understanding the Problem

The first stage of the project was understanding the rules of the Game of Pig and analyzing the provided skeleton program. The objective was to create a Human vs Computer version of the game while preserving the original structure as much as possible.

One of the first concepts I identified was the balance between risk and reward. Players can continue rolling to earn more points during a turn, but rolling a **1** immediately ends the turn and all points earned during that round are lost. Understanding this rule helped determine the overall program logic and the sequence of decisions that both the player and the computer would make.

At this stage I also identified the main components required for the program, including score management, player turns, computer turns, and the main game loop.

<br>

## Planning and Design

Before writing code, I planned the overall structure of the application using modular programming principles.

Instead of writing everything inside one large program, I divided the project into independent functions, each responsible for a single task. This approach makes the code easier to understand, maintain, and debug.

The primary functions include:

- `roll_die()`
- `player_turn_manual()`
- `player_turn_auto()`
- `computer_turn()`
- `check_winner()`
- `choose_mode()`
- `game()`

During planning, I also created a simple pseudocode outline to visualize the flow of the game. One challenge was preventing infinite loops while allowing the game to continue until a player reached 100 points. This was solved by designing a main game loop with clear exit conditions whenever a winner is detected.

<br>

## Implementation

The implementation phase focused on translating the design into a working Python program.

The dice rolling mechanism was implemented using Python's built-in **random** module. Player interaction was then added, allowing the user to decide whether to continue rolling or hold after each successful roll.

During development, I encountered an issue where the player's turn sometimes failed to exit correctly, causing the game to remain inside the turn loop. This problem was solved by restructuring the function and using `return` statements to clearly terminate the player's turn whenever necessary.

This stage reinforced the importance of function design and proper control flow.
