
import random
import board_manager as b

def spawn_tile(board):
    #spawns a random 2 or 4 in an empty cell
    b.spawn_random_tile(board)

def compress_line(line):
    #Slides all non-zero tiles to one side
    # 0 2 0 4 -> 0 0 2 4 / 2 4 0 0 
    non_zeros = [l for l in line if l != 0]
    return non_zeros + [0]*(len(line) - len(non_zeros))        

def merge_line(line):
    #Merge equal adjacent tiles and return new row
    line = compress_line(line)
    for i in range(len(line)-1):
        if line[i] == line[i+1] and line[i] != 0:
            line[i] = 2*line[i] 
            b.SCORE = b.SCORE + line[i]
            line[i+1] = 0
    return compress_line(line)

def transpose(board):
    num_cols = len(board[0])
    board[:] = [[row[i] for row in board] for i in range(num_cols)]

def move(board, direction):
    #Move tiles in the specified direction (up/down/left/right)
    num_rows = len(board)
    num_cols = len(board[0])
    
    board_copy = []
    for i in range(num_rows):
        board_copy.append([])
    for i in range(num_rows):
        for j in range(num_cols):
            board_copy[i].append(board[i][j])


    if direction == "Left":
        for i in range(num_rows):
            board[i] = merge_line(board[i])
    
    if direction == "Right":
        for i in range(num_rows):
            board[i] = board[i][::-1]
            board[i] = merge_line(board[i])
            board[i] = board[i][::-1]

    if direction == "Up":
        transpose(board)
        move(board, "Left")
        transpose(board)

    if direction == "Down":
        transpose(board)
        move(board, "Right")
        transpose(board)

    return board_copy != board

def check_game_state(board):
    """
    returns
        won if 2048 tile exists,
        lost if no valid moves remain,
        continue otherwise.
    """
    num_cols = len(board[0])
    num_rows = len(board)
    
    for i in range(num_rows):
        if 2048 in board[i]:
            return "WON"
        
    board_copy = []
    for i in range(num_rows):
        board_copy.append([])
    for i in range(num_rows):
        for j in range(num_cols):
            board_copy[i].append(board[i][j])
    print(board_copy)
    print(move(board_copy, "Left"))


    if not (move(board_copy, "Left") or move(board_copy, "Right") or move(board_copy, "Up") or move(board_copy, "Down")):
        return "LOST"
    return "CONTINUE"
    
   

if __name__ == "__main__":
    # print(merge_line([0, 2, 2, 2]))
    
    # goal : check continue
    board1 = [[4, 16, 2, 16],
              [8, 8, 8, 4],
              [4, 4, 4, 2],
              [2, 2, 2, 4]]
    
    # goal: check lost, neighbours musn't be same
    board2 = [[2, 16, 4, 16],
              [8, 4, 8, 4],
              [4, 16, 4, 2],
              [2, 64, 2, 4]]
    #transpose(board)
    #move(board, "up")
    print(check_game_state(board1))
    print(check_game_state(board2))

    #print(move(board, "Left"))
    #print(board)
