# 2048 

A Python‑based implementation of 2048 built using Tkinter for the GUI.

# Game Description

The goal is to slide numbered tiles on a grid to combine them and create
a tile with the number 2048. When two tiles with the same number touch,
they merge into one. The game ends when no moves are possible.

# Features

-   Supports tile moves (up/down/left/right) via keyboard input.
-   Merging logic to combine matching tiles.
-   Score tracking.
-   Save/load functionality

# Setup & Installation

1.  Ensure you have Python installed.

2.  Clone the repository:

    ``` bash
    git clone https://github.com/dhruvsambavaram/2048.git
    cd 2048
    ```
3.  Run the game:

    ``` bash
    python main.py
    ```

# Game instructions

-   Use the arrow keys (↑ ↓ ← →) to move the tiles.
-   When two tiles with the same value collide in the move, they merge
    into one tile with value = sum of both.
-   Merged tiles count toward your score.
-   New tiles appear after each move.
-   The game ends when there are no valid moves left.

# Project Structure

    2048/
    ├── board_manager.py     # GUI rendering and UI events
    ├── file_manager.py      # Saving/loading state
    ├── game_logic.py        # Board state, move logic, merge logic
    ├── main.py              # Entry point to start the game
    └── README.md            # This file

