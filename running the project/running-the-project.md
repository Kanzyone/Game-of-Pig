# Running the Project

To run this project on your local machine, you will need **Python 3** installed. No additional libraries or third-party packages are required because the project only uses Python's built-in modules (`random` and `time`).

Begin by cloning the repository to your computer using the following command:

```bash
git clone https://github.com/Kanzyone/Game-of-Pig.git
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
