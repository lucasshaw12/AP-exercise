import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells
nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')
        else:
            column.append(' ')
    nextCells.append(column) # nextCells is a list of column lists

while True:
    print('\n\n\n')
    currentCells = copy.deepcopy(nextCells)

    # Print current cells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print() # print a new line at the end of the row

    # Calculate the next steps cells based on the current step cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count the living neighbours
            numNeighbours = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbours += 1 # Top left neighbour is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbours += 1 # Top neighbour is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbours += 1 # top right neighbour is alive
            if currentCells[leftCoord][y] == '#':
                numNeighbours += 1 # left neighbour is alive
            if currentCells[rightCoord][y] == '#':
                numNeighbours += 1 # right neighbour is alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbours += 1 # bottom left neighbour is alive
            if currentCells[x][belowCoord] == '#':
                numNeighbours += 1 # bottom neighbour is alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbours += 1 # bottom right neighbour is alive

            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbours == 2 or numNeighbours == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbours == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(.01)      














