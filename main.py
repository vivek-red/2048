# main.py
import tkinter as tk
import board_manager as b
import game_logic as g
import file_manager as f

LABELS = []
GAME_STATE = "CONTINUE"
commands = {
            'Up'   : g.move, 
            'Down' : g.move,
            'Left' : g.move,
            'Right': g.move
        }

#GUI Colour mapping
CELL_COLORS = {
    0: "#cdc1b4",
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",      
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e"
}
CELL_NUMBER_COLORS = {2: "#776e65", 4: "#776e65"}
CELL_NUMBER_FONT = ("Verdana", 24, "bold")
TITLE_FONT = ("Verdana", 28, "bold")
BOARD_BG = "#bbada0"
EMPTY_CELL = "#cdc1b4"
BUTTON_BG = "#8f7a66"
BUTTON_FG = "#f9f6f2"
BUTTON_ACTIVE_BG = "#9c8571"
SCORE_BG = "#5b3e23"
SCORE_FG = "#f9f6f2"
TITLE_FG = "#eee4da"

def game_over_screen():
    print(GAME_STATE)
    over = tk.Toplevel(root)
    over.title("Game Over 😭")
    tk.Label(over, text="Game Over!", font=("Verdana", 20, "bold")).pack(pady=20)

def game_won_screen():
        over = tk.Toplevel(root)
        over.title("Game won !!!")
        tk.Label(over, text="Game won!", font=("Verdana", 20, "bold")).pack(pady=20)

def display_board(board):
    num_rows = len(board)
    num_cols = len(board[0])
    for i in range(num_rows):
        for j in range(num_cols):
            LABELS[4*i + j].config(text = str(board[i][j]), bg = CELL_COLORS[board[i][j]])
    score_value_label.config(text = str(b.SCORE))

def new_game():
    global board
    board = b.init_board()
    display_board(board)

def save_game():
    f.save_game(board)
    f.save_score()

def load_game():
    global board
    board = f.load_game()
    b.SCORE = f.load_score()
    display_board(board)

def key_pressed(event):
    global GAME_STATE
    if GAME_STATE == "CONTINUE":
        key = event.keysym
        if key in commands.keys():
            
            # operation
            commands[key](board, key)
            
            # feasability
            GAME_STATE = g.check_game_state(board)
            
            if GAME_STATE == "CONTINUE":
                b.spawn_random_tile(board)
                print(g.check_game_state(board))
            
            elif GAME_STATE == "WON":
                game_won_screen()

            display_board(board)

            if GAME_STATE == "LOST":
                game_over_screen()
         
if __name__ == "__main__":
    #main()
    root = tk.Tk()
    root.bind("<Key>", key_pressed)
    root.title("2048")

    board = b.init_board()

    score_frame = tk.Frame(root)
    score_frame.grid(row = 0, column = 0, sticky = "ew", padx = 20, pady = 20)

    game_label = tk.Label(score_frame, text = "2048 GAME", borderwidth = 1, width = 10, height = 3, justify= tk.LEFT, font= TITLE_FONT )
    game_label.grid(row = 1, column = 0, sticky = "w")


    dummy_label = tk.Label(score_frame, text = "   ", width = 25, height = 3)
    dummy_label.grid(row = 1, column = 1, padx = 5, pady = 5)

    score_tittle_label = tk.Label(score_frame, text = "Score:", borderwidth = 1, width = 10, height = 3, justify= tk.CENTER, font= CELL_NUMBER_FONT )
    score_tittle_label.grid(row = 1, column = 2, padx = 5, pady = 5)

    score_value_label = tk.Label(score_frame, text = str(b.SCORE), borderwidth = 1, width = 10, height = 3, justify= tk.CENTER, bg = CELL_COLORS[0], font= CELL_NUMBER_FONT )
    score_value_label.grid(row = 1, column = 3, padx = 5, pady = 5)

    btns_frame = tk.Frame(root)
    btns_frame.grid(row = 2, column = 0, padx = 20, pady = 20)

    new_game_btn = tk.Button(btns_frame, text = "New Game", command = new_game, font=("Verdana", 11, "bold"),
        padx=16,
        pady=10,
        fg=BUTTON_FG,
        bg=BUTTON_BG,
        activebackground=BUTTON_ACTIVE_BG,)
    new_game_btn.grid(row = 1, column = 0, padx = 5, pady = 5)

    save_btn = tk.Button(btns_frame, text = "Save", command = save_game, font=("Verdana", 11, "bold"),
        padx=16,
        pady=10,
        fg=BUTTON_FG,
        bg=BUTTON_BG,
        activebackground=BUTTON_ACTIVE_BG,)
    save_btn.grid(row = 1, column = 1, padx = 5, pady = 5)

    load_btn = tk.Button(btns_frame, text = "Load", command = load_game, font=("Verdana", 11, "bold"),
        padx=16,
        pady=10,
        fg=BUTTON_FG,
        bg=BUTTON_BG,
        activebackground=BUTTON_ACTIVE_BG,)
    load_btn.grid(row = 1, column = 2, padx = 5, pady = 5)


    board_frame = tk.Frame(root, bg = "#bbada0")
    board_frame.grid(row = 1, column = 0, padx = 20, pady = 20)
    for i in range(4):
        for j in range(4):
            label = tk.Label(board_frame, text = str(board[i][j]), borderwidth = 1, width = 10, height = 3, justify= tk.CENTER, bg = CELL_COLORS[0], font= CELL_NUMBER_FONT )
            label.grid(row = i, column = j, padx = 5, pady = 5)
            LABELS.append(label)

    root.mainloop()
