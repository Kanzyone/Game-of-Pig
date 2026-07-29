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

<br>

## Computer Logic and Testing

Once the player mechanics were complete, I developed the computer opponent.

The computer follows a simple strategy by continuing to roll until it earns approximately **20 points** during a turn or until stopping would allow it to win the game. Although intentionally simple, this strategy creates a balanced opponent while keeping the program readable.

Testing revealed several logical issues, particularly involving score updates and turn transitions. These were resolved by carefully tracing returned values, verifying score calculations, and ensuring that turns always alternate in the correct order.

Repeated testing played an important role in improving the reliability of the final program.

<br>

## Final Improvements

After the core gameplay was complete, several quality-of-life improvements were added to make the game more enjoyable and easier to use.

The final version includes:

- Manual and automatic gameplay modes
- Input validation
- Replay functionality
- Improved console formatting
- A refined computer strategy

These additions were made after the main functionality was complete, demonstrating the importance of refining software beyond simply making it work

<br>

## What I Learned

This project significantly improved my understanding of the complete software development process.

Throughout development, I practiced breaking complex problems into smaller tasks, designing reusable functions, debugging logical errors, validating user input, and improving program organization.

More importantly, I learned that writing software is an iterative process. Careful planning, continuous testing, and gradual improvements are just as important as writing the initial code.

<br>
<br>

# Running the Project

To run this project on your local machine, you will need **Python 3** installed. No additional libraries or third-party packages are required because the project only uses Python's built-in modules (`random` and `time`).

Begin by cloning the repository to your computer using the following command:

```bash
git clone https://github.com/yourusername/Game-of-Pig.git
```

Navigate into the project directory:

```bash
cd Game-of-Pig
```

Run the program using Python:

```bash
python game_of_pig.py
```

Once the program starts, you will be prompted to choose between **Manual Mode** and **Automatic Mode**.

- **Manual Mode** allows you to decide whether to roll the die or hold after each successful roll.
- **Automatic Mode** continuously rolls the die until the turn ends, making it useful for quickly observing the game mechanics.

The game alternates turns between the player and the computer until one of them reaches **100 points**. At the end of each game, you will have the option to start a new game or exit the program.

<br>

Was used in this project:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![edX](https://img.shields.io/badge/edX-%2302262B.svg?style=for-the-badge&logo=edX&logoColor=white) ![Khan Academy](https://img.shields.io/badge/KhanAcademy-%2314BF96.svg?style=for-the-badge&logo=KhanAcademy&logoColor=white)
