# Conway's game of life
import random, time, copy
WIDTH = 60
HEIGHT = 20

# create a list for the cells:
nextCells = []
for x in range(WIDTH):
    column = []  # create a new column
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append("#")  # add a living cell
        else:
            column.append("")  # add a dead cell
    nextCells.append(column)  # nextCells is a list of column lists

while True:  # Main program loop
    print("\n\n\n\n\n")  # seperate each step with new lines
    currentCells = copy.deepcopy(nextCells)
    # Print currentCells on screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end="")  # Print the # or space
        print()  # Print a new line at the end of the row

    # Calculate the next step's cells based on the current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighbouring cooordinates:
            # % WIDTH ensures leftCoord is always between 0 and WIDTH -1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neighbours
            numNeighbours = 0
            if currentCells[leftCoord][aboveCoord] == "#":
                numNeighbours += 1  # Top left neighbour is alive
            if currentCells[x][aboveCoord] == "#":
                numNeighbours += 1  # Top neighbour is alive
            if currentCells[rightCoord][aboveCoord] == "#":
                numNeighbours += 1  # Top right neighbour is alive
            if currentCells[leftCoord][y] == "#":
                numNeighbours += 1  # left neighbour is alive
            if currentCells[rightCoord][y] == "#":
                numNeighbours += 1  # Right neighbour is alive
            if currentCells[leftCoord][belowCoord] == "#":
                numNeighbours += 1  # Bottom left neighbour is alive
            if currentCells[x][belowCoord] == "#":
                numNeighbours += 1  # Bottom neighbour is alive
            if currentCells[rightCoord][belowCoord] == "#":
                numNeighbours += 1  # Bottom-right neighbour is alive

            # Set cell based on Conway's game of life rules:
            if currentCells[x][y] == "#" and (numNeighbours == 2 or numNeighbours == 3) :
                # living cells with 2 or 3 neighbours stay alive:
                nextCells[x][y] = "#"
            elif currentCells[x][y] == "" and numNeighbours == 3:
                nextCells[x][y] = "#"
            else:
                # Everything else dies or stays dead:
                 nextCells[x][y] = ""
        time.sleep(1)  # Add a one second pause to reduce flickering
                
       
        

