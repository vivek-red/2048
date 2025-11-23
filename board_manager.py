import random
SCORE = 0

# board.py (public API)
def create_board(size: int = 4) -> list[list[int]]:
    #Returns a board filled with zeros
    board = []
    for i in range(size):
        board = board + [[0 for j in range(size)]]
    return board

def random_tile_value(rng  = random) -> int:
    #Return 2 or 4 based on the spawn probability
    a = rng.randint(0, 9)
    if a in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        return 2
    return 4


def spawn_random_tile(board: list[list[int]], rng=random) -> tuple[int,int]:
    """Places a new tile into a random empty cell
       Returns the row and col where it was placed
       gives error if no empty cells."""
    if 0 in board[0] or 0 in board[1] or 0 in board[2] or 0 in board[3]:  
        while True:
            a = rng.randint(0, 15)
            row = a//4
            col = a%4
            if board[row][col] == 0:
                break
        board[row][col] = random_tile_value(rng)
        return (row, col)
       
def init_board(size: int = 4, rng=random) -> list[list[int]]:
    #Create board, spawn two tiles, return board
    board = create_board()
    global SCORE
    SCORE = 0
    spawn_random_tile(board, rng)
    spawn_random_tile(board, rng)
    return board


def board_to_string(board: list[list[int]]) -> str:
    #Returns a string version of the board printed into the CLI
    return "\n".join(" ".join(str(col) for col in row) for row in board)

def print_board(board: list[list[int]]) -> None:
    #Print board_to_string(board)
    print(board_to_string(board))

def save_board(board: list[list[int]], file_name: str):
    with open(file_name, "w") as f:
        f.write(board_to_string(board))

def load_board(file_name: str)-> list[list[int]]:
    #1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16
    with open(file_name, "r") as f:
        board_str = f.read()
        rows = board_str.split("\n")
        board = [list(map(int, row.split(" "))) for row in rows]
        return board
    
if __name__ == "__main__":
    #board = init_board()
    #print(board)
    #save_board(board, "1.txt")
    print(load_board("1.txt"))
