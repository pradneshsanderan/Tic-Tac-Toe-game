# the list containing all inputs for the game board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-", ]

# determines if the game is still going or has ended. becomes False when someone has won or there is a tie
game_still_going = True

# displays the winner of the game. if the game is still going, the winner is none
winner = None

# the current player who's turn it is
current_player = "X"


# displays the board with all inputs. if a position is empty, a '-' is diplayed
def displayBoard():
    print("-------------")
    print("|  " + board[0] + " | " + board[1] + " |  " + board[2] + " |")
    print("-------------")
    print("|  " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("|  " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")


# the main method for the flow of the game
def play_game():
    displayBoard()

    # while no one has won or it is not a tie, the game goes on
    while game_still_going:
        # the player plays his turn
        handle_turn(current_player)

        # checks if someone has won
        check_if_game_over()

        # if someone has won, the winner is displayed
        if winner == "X" or winner == "O":
            print(winner + " won")
        # if it is a tie, the game states it
        elif check_if_tie():
            print("Tie.")
        # if no one has won and it is not a tie, the players turns are switched
        flip_player()


# method to handle the player who's turn it is
def handle_turn(player):
    # shows which player's turn it is
    print(player + "'s turn.")
    # player has to input the position they choose
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        # checks if the input is a valid integer
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid Input. Choose a position from 1-9: ")

        position = int(position) - 1
        # checks if the position on the board is empty or not
        if board[position] == "-":
            valid = True
        else:
            print("you can't go there. go again")

    # updates the position chosen by the player with the player's symbol
    board[position] = player
    displayBoard()


# method to check if the game has ended or not
def check_if_game_over():
    check_if_Win()
    check_if_tie()


# method to check if someone has won the game or not
def check_if_Win():
    global winner
    row_winner = check_rows()
    column_winner = check_colums()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


# method to check each row if the symbols in the row are the same and someone has won
def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]


# method to check each column if the symbols in the column are the same and someone has won
def check_colums():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]


# method to check each diagonal if the symbols in the diagonal are the same and someone has won
def check_diagonals():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[1]


# method to check if the game has ended in a tie
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
        return True
    else:
        return False


# method to change the players turn once the other player has done their turn
def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


play_game()
