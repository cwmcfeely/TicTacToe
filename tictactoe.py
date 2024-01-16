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
    print(" " + gameBoard[0] + " | " + gameBoard[1] + " | " + gameBoard[2])
    print("-----------")
    print(" " + gameBoard[3] + " | " + gameBoard[4] + " | " + gameBoard[5])
    print("-----------")
    print(" " + gameBoard[6] + " | " + gameBoard[7] + " | " + gameBoard[8])
printGameBoard(gameBoard)

# Function to take players input
def playerInput(gameBoard):
    playerIn = int(input("Enter a number 1-9: ")) # Need to use int conversion as input outputs as string
    if playerIn >= 1 and playerIn <=9 and gameBoard[playerIn-1] == "-":
        gameBoard[playerIn-1] = currentPlayer
    else:
        print("That move has already been taken!")


# Checking for horizontal win or tie
def checkHorizontal(gameBoard):
    global winner # Global will change the scope to the whole file, not just the function
    if gameBoard[0] == gameBoard[1] == gameBoard[2] and gameBoard[1] != "-":
        winner = gameBoard[0]
        return True
    elif gameBoard[3] == gameBoard[4] == gameBoard[5] and gameBoard[3] != "-":
        winner = gameBoard[3]
        return True
    elif gameBoard[5] == gameBoard[6] == gameBoard[7] and gameBoard[5] != "-":
        winner = gameBoard[5]
        return True
    
# Checking for row win or tie   
def checkRow(gameBoard):
    global winner # Global will change the scope to the whole file, not just the function
    if gameBoard[0] == gameBoard[3] == gameBoard[5] and gameBoard[0] != "-":
        winner = gameBoard[0]
        return True
    elif gameBoard[1] == gameBoard[4] == gameBoard[6] and gameBoard[1] != "-":
        winner = gameBoard[1]
        return True
    elif gameBoard[2] == gameBoard[5] == gameBoard[7] and gameBoard[2] != "-":
        winner = gameBoard[2]
        return True

# Checking for diagnaol win or tie   
def checkRow(gameBoard):
    global winner # Global will change the scope to the whole file, not just the function
    if gameBoard[0] == gameBoard[4] == gameBoard[7] and gameBoard[0] != "-":
        winner = gameBoard[0]
        return True
    elif gameBoard[2] == gameBoard[4] == gameBoard[5] and gameBoard[2] != "-":
        winner = gameBoard[2]
        return True

# Checking for a tie game, only need to check to see if there is not a blank space   
def checkTieGame(gameBoard):
    global gameRunning
    if "-" not in gameBoard:
        printGameBoard(gameBoard)
        print("It's a time game")
        gameRunning = False


while gameRunning:
    printGameBoard(gameBoard)
    playerInput(gameBoard)