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