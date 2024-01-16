import random

print(" ")
print("***********************")
print("***** Tic-Tac-Toe *****")
print("***********************")
print(" ")

# function to print the board to command line
def print_game_board(game_board):
    print(" ")
    print(" " + game_board[0] + " | " + game_board[1] + " | " + game_board[2])
    print("-----------")
    print(" " + game_board[3] + " | " + game_board[4] + " | " + game_board[5])
    print("-----------")
    print(" " + game_board[6] + " | " + game_board[7] + " | " + game_board[8])
    print(" ")

# Function to take players input
def player_input(game_board):
    try:
        while True:
            playerIn = int(input(f"Player {current_player} Enter a number 1-9: ")) # Need to use int conversion as input outputs as string
            if playerIn >= 1 and playerIn <=9 and game_board[playerIn-1] == "-":
                game_board[playerIn-1] = current_player
                break
            elif playerIn < 1 or playerIn > 9:
                print("Please only enter a number betweem 1-9 and try again")
            else:
                print("That move has already been taken!")
    except ValueError:
        print("Please only enter a number 1-9 and try again")


# Checking for horizontal win or tie
def check_horizontal(game_board):
    global winner # Global will change the scope to the whole file, not just the function
    if game_board[0] == game_board[1] == game_board[2] and game_board[0] != "-":
        winner = game_board[0]
        return True
    elif game_board[3] == game_board[4] == game_board[5] and game_board[3] != "-":
        winner = game_board[3]
        return True
    elif game_board[6] == game_board[7] == game_board[8] and game_board[6] != "-":
        winner = game_board[6]
        return True
    
# Checking for row win or tie   
def check_vertical(game_board):
    global winner # Global will change the scope to the whole file, not just the function
    if game_board[0] == game_board[3] == game_board[6] and game_board[0] != "-":
        winner = game_board[0]
        return True
    elif game_board[1] == game_board[4] == game_board[7] and game_board[1] != "-":
        winner = game_board[2]
        return True
    elif game_board[2] == game_board[5] == game_board[8] and game_board[2] != "-":
        winner = game_board[2]
        return True

# Checking for diagnaol win or tie   
def check_diagonal(game_board):
    global winner # Global will change the scope to the whole file, not just the function
    if game_board[0] == game_board[4] == game_board[8] and game_board[0] != "-":
        winner = game_board[0]
        return True
    elif game_board[2] == game_board[4] == game_board[6] and game_board[2] != "-":
        winner = game_board[2]
        return True

# Checking for a tie game, only need to check to see if there is not a blank space   
def check_tie_game(game_board):
    global game_running
    if "-" not in game_board and not check_diagonal(game_board) and not check_horizontal(game_board) and not check_vertical(game_board):
        print_game_board(game_board)
        print("It's a time game!")
        game_running = False

# Checking for the winner
def check_who_won():
    global game_running
    if check_diagonal(game_board) or check_horizontal(game_board) or check_vertical(game_board):
        print_game_board(game_board)
        print(f"Congratualtions, The winner is player {winner}!")
        game_running = False

# Create a function that switches between each players turn
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def player_computer(game_board):
    while current_player == "O":
        for i in range(9):
            if game_board[i] == "-":
                # Simulate making a move at blank positions for computer player
                game_board[i] = "O"
                # This if statement will check if there is any winning moves for the computer player
                if check_diagonal(game_board) or check_horizontal(game_board) or check_vertical(game_board):
                    switch_player()
                    return
                # If it's not a winning move, return it back to a blank position
                game_board[i] = "-"
        # This range will looks for positions to block player1 from using
        for i in range(9):
            if game_board[i] == "-":
                # Simulate making a move at the position for the player
                game_board[i] = "X"
                if check_diagonal(game_board) or check_horizontal(game_board) or check_vertical(game_board):
                    game_board[i] = "O"
                    switch_player()
                    return
                game_board[i] = "-"

        # If there is no winning or blocking move, make a random move
        position = random.randint(0, 8)
        if game_board[position] == "-":
            game_board[position] = "O"
            switch_player()

def reset_game():
    global game_board, current_player, winner, game_running
    # Creating the game board
    game_board = ["-","-","-",
                  "-","-","-",
                  "-","-","-"]
    current_player = 'X'
    winner = None
    game_running = True

while True:
    reset_game()
    
    while game_running:
        print_game_board(game_board)
        player_input(game_board)
        check_who_won()
        check_tie_game(game_board)
        if not game_running:
            break
        switch_player()
        player_computer(game_board)
        check_who_won()
        check_tie_game(game_board)

    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again != "yes":
        print("Thank for playing, Goodbye!")
        break