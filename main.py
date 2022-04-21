#game_board
board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]

#game running?
game_running = True

#won or tie?
winner = None

#who's turn?
current_player = "X"

#count of turns
count = 0

#display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#play the game of tic tac toe
def play_game():

    global count

    #display the initial board
    display_board()



    #when game is still going on
    while game_running:

        #handle the turn
        handle_turn(current_player)

        #check if game is over
        check_game_over()

        #pass turn to other player
        pass_player()

        count += 1

    #when game ends
    if winner == "X" or winner == "O":
        print(winner + " Won.")
    elif winner == None:
        print("Tie.")
    
#handle the turn
def handle_turn(player):

    global count

    print(player + "'s turn")

    #turn handling only valid till 8th turn
    if count < 8: 
        
        position = int(input("Choose a position from 1-9: "))

        valid = False
        while not valid:

            while position not in list(range(1, 10)):
                position = int(input("Invalid Input. Choose a position from 1-9: "))

            position = int(position) - 1

            if board[position] == "-":
                valid = True
            else:
                print("The place is already filled. Go again")

        board[position] = player
        
    else:
        board[board.index("-")] = 'X'
        

    display_board()


def check_game_over():
    check_win()
    check_tie()


def check_win():

    #set up global variables
    global winner

    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return



def check_rows():

    global game_running

    #check if rows have same values and not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    #if any row matches than assign it win
    if row_1 or row_2 or row_3:
        game_running = False

    #return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return


def check_columns():

    global game_running

    #check iff columns have same values and not empty
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    #if any column matches than assign it win
    if col_1 or col_2 or col_3:
        game_running = False

    #return the winner
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]

    return


def check_diagonals():

    global game_running

    #check iff diagonal have same values and not empty
    dig_1 = board[0] == board[4] == board[8] != "-"
    dig_2 = board[6] == board[4] == board[2] != "-"

    #if any diagonal matches than assign it win
    if dig_1 or dig_2:
        game_running = False

    #return the winner
    if dig_1:
        return board[4]
    elif dig_2:
        return board[4]

    return


def check_tie():

    global game_running

    if "-" not in board:
        game_running = False

    return


def pass_player():

    global current_player

    #if current is X change O
    if current_player == "X":
        current_player = "O"
    #if current is O then change X
    elif current_player == "O":
        current_player = "X"
    return

play_game()


#board
#display board
#play game
    #turn handler
#check win
    #check rows
    #check columns
    #check diagonals
#check tie
#pass player
