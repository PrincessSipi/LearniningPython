"""
tic tac toe board
[
    [-, -, -],
    [-, -, -],
    [-, -, -]
]

user input -> something 1-9
If they enter anything else tell them to go again
check if the user input is already taken
add it to the board
check if the user won: checking rows, columns and diagonals
toggle between users upon successful moves
"""
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
    ]

def printBoard(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end=" ")
        print()  
            
printBoard(board)

def quit(user_input):
    if user_input == "q":
        print("Thanks for playing!!")
        return True
    else:
        return False

def check_input(user_input):
    # check if its a number
   if not isnum(user_input):
       return False
   user_input = int(user_input)
    # check if its 1-9
   if not boundary(user_input):
        return False
   return True

def boundary(user_input):
    if user_input > 9 or user_input < 1:
        print( "This is out of range!!")
        return False
    else:
        return True
    
def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number!!")
        return False
    else:
        return True

def isTaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":

    
def coordinates(user_input):
    row = int(user_input) / 3
    col = user_input
    if col > 2:
        col = int (col % 3)
        return (row,col)

while True:
    printBoard(board)
    user_input = input("Please enter a position 1 through 9 or enter\"q\" to quit \t")
    if quit(user_input): break
    if not check_input(user_input):
        print("Please try again!! ")
        continue
    user_input = int(user_input)-1
    coords = coordinates(user_input)
