# Create a board
board=[" - "," - "," - ",
       " - "," - "," - ",
       " - "," - "," - "]

# Is game still going
game_still_going=True

# Who won or is it  tie
winner=None

# Whose turn?
current_player=' X '

# Display board
def display_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

# Condition to check whether the game is over
def check_if_game_over():
    check_for_winner()
    check_if_tie()

#Check if win
def check_for_winner():
    # Setup the global variable
    global winner
    # check row
    row_winner=check_row()

    # check column
    column_winner=check_column()

    # check diagonals
    diagonal_winner=check_diagonal()

    # Get the winner
    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None
    return
def check_row():
    # Setup the global variable
    global game_still_going

    #check if any of the rows have the same value and not empty
    row_1=board[0]==board[1]==board[2]!=' - '
    row_2 = board[3] == board[4] == board[5] != ' - '
    row_3 = board[6] == board[7] == board[8] != ' - '
    if row_1 or row_2 or row_3:
        game_still_going=False

    # Return the winner(X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return
def check_column():
    # Setup the global variable
    global game_still_going

    # check if any of the columns have the same value and not empty
    column_1 = board[0] == board[3] == board[6] != ' - '
    column_2 = board[1] == board[4] == board[7] != ' - '
    column_3 = board[2] == board[5] == board[8] != ' - '
    if column_1 or column_2 or column_3:
        game_still_going = False

    # Return the winner(X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return
def check_diagonal():
    # Setup the global variable
    global game_still_going

    # check if any of the diagonals have the same value and not empty
    diagonal_1 = board[0] == board[4] == board[8] != ' - '
    diagonal_2 = board[2] == board[4] == board[6] != ' - '
    if diagonal_1 or diagonal_2:
        game_still_going = False

    # Return the winner(X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return
# Check for tie
def check_if_tie():
    global game_still_going
    if " - " not in board:
        game_still_going=False
    return

# Flip to other player
def flip_player():
    global current_player

    if current_player==" X ":
        current_player=" O "
    elif current_player==" O ":
        current_player=" X "
    return

# Play a game of tic tac toe
def play_game():
    # Initially display the board
    display_board()

    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    # When game ends
    if winner==" X " or winner==" O ":
        print(winner+" won.")
    elif winner==None:
        print("Tie.")

# Handle a single turn of an arbitrary player
def handle_turn(player):
    print(player+"'s turn.")
    position=(input("choose a position from 1-9: "))
    valid=False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = (input("choose a position from 1-9: "))
        position=int(position)-1
        if board[position]==" - ":
            valid=True
        else:
            print("You cant go there.Try new input")
    board[position]=player
    display_board()
play_game()

