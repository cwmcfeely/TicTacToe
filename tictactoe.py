import random

print("***********************")
print("***** Tic-Tac-Toe *****")
print("***********************")
# Creating the game board
gameBoard = ["-","-","-",
             "-","-","-",
             "-","-","-"]

# Some Global variables
currentPlayer = 'X'
winner = None
gameRunning = True

# function to print the board to command line
def printGameBoard(gameBoard):
    print(" ")
    print(" " + gameBoard[0] + " | " + gameBoard[1] + " | " + gameBoard[2])
    print("-----------")
    print(" " + gameBoard[3] + " | " + gameBoard[4] + " | " + gameBoard[5])
    print("-----------")
    print(" " + gameBoard[6] + " | " + gameBoard[7] + " | " + gameBoard[8])
    print(" ")

# Function to take players input
def playerInput(gameBoard):
    try:
        while True:
            playerIn = int(input(f"Player {currentPlayer} Enter a number 1-9: ")) # Need to use int conversion as input outputs as string
            if playerIn >= 1 and playerIn <=9 and gameBoard[playerIn-1] == "-":
                gameBoard[playerIn-1] = currentPlayer
                break
            elif playerIn < 1 or playerIn > 9:
                print("Please only enter a number betweem 1-9 and try again")
            else:
                print("That move has already been taken!")
    except ValueError:
        print("Please only enter a number 1-9 and try again")


# Checking for horizontal win or tie
def checkHorizontal(gameBoard):
    global winner # Global will change the scope to the whole file, not just the function
    if gameBoard[0] == gameBoard[1] == gameBoard[2] and gameBoard[0] != "-":
        winner = gameBoard[0]
        return True
    elif gameBoard[3] == gameBoard[4] == gameBoard[5] and gameBoard[3] != "-":
        winner = gameBoard[3]
        return True
    elif gameBoard[6] == gameBoard[7] == gameBoard[8] and gameBoard[6] != "-":
        winner = gameBoard[6]
        return True
    
# Checking for row win or tie   
def checkVertical(gameBoard):
    global winner # Global will change the scope to the whole file, not just the function
    if gameBoard[0] == gameBoard[3] == gameBoard[6] and gameBoard[0] != "-":
        winner = gameBoard[0]
        return True
    elif gameBoard[1] == gameBoard[4] == gameBoard[7] and gameBoard[1] != "-":
        winner = gameBoard[2]
        return True
    elif gameBoard[2] == gameBoard[5] == gameBoard[8] and gameBoard[2] != "-":
        winner = gameBoard[2]
        return True

# Checking for diagnaol win or tie   
def checkDiagonal(gameBoard):
    global winner # Global will change the scope to the whole file, not just the function
    if gameBoard[0] == gameBoard[4] == gameBoard[8] and gameBoard[0] != "-":
        winner = gameBoard[0]
        return True
    elif gameBoard[2] == gameBoard[4] == gameBoard[6] and gameBoard[2] != "-":
        winner = gameBoard[2]
        return True

# Checking for a tie game, only need to check to see if there is not a blank space   
def checkTieGame(gameBoard):
    global gameRunning
    if "-" not in gameBoard and not checkDiagonal(gameBoard) and not checkHorizontal(gameBoard) and not checkVertical(gameBoard):
        printGameBoard(gameBoard)
        print("It's a time game!")
        gameRunning = False

# Checking for the winner
def checkWhoWon():
    global gameRunning
    if checkDiagonal(gameBoard) or checkHorizontal(gameBoard) or checkVertical(gameBoard):
        printGameBoard(gameBoard)
        print(f"Congratualtions, The winner is player {winner}!")
        gameRunning = False

# Create a function that switches between each players turn
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def playerComputer(gameBoard):
    while currentPlayer == "O":
        for i in range(9):
            if gameBoard[i] == "-":
                # Simulate making a move at blank positions for computer player
                gameBoard[i] = "O"
                # This if statement will check if there is any winning moves for the computer player
                if checkDiagonal(gameBoard) or checkHorizontal(gameBoard) or checkVertical(gameBoard):
                    switchPlayer()
                    return
                # If it's not a winning move, return it back to a blank position
                gameBoard[i] = "-"
        # This range will looks for positions to block player1 from using
        for i in range(9):
            if gameBoard[i] == "-":
                # Simulate making a move at the position for the player
                gameBoard[i] = "X"
                if checkDiagonal(gameBoard) or checkHorizontal(gameBoard) or checkVertical(gameBoard):
                    gameBoard[i] = "O"
                    switchPlayer()
                    return
                gameBoard[i] = "-"

        # If there is no winning or blocking move, make a random move
        position = random.randint(0, 8)
        if gameBoard[position] == "-":
            gameBoard[position] = "O"
            switchPlayer()

while gameRunning:
    printGameBoard(gameBoard)
    playerInput(gameBoard)
    checkWhoWon()
    checkTieGame(gameBoard)
    if not gameRunning:
        break
    switchPlayer()
    playerComputer(gameBoard)
    checkWhoWon()
    checkTieGame(gameBoard)