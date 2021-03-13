from data.map import Map
import numpy as np

# Makes a new map initialized with -1 in every location
def startState (matrix_size) -> Map:
    new_map = Map()
    new_map.map_size = matrix_size
    new_map.map_state = [
        [-1 for x in range(matrix_size)] for y in range(matrix_size)
    ]

    return new_map
    
# Returns the characters for the border frame of the game board
def getFrame (map_size):
    frame = '+'
    for i in range(map_size):
        frame = frame + '---+'

    return frame
    
# Returns the characters for the numerical column labels
def getLegend (map_size):
    frame = ''
    for i in range(map_size):
        frame = frame + '  ' + str(i+1) + ' '

    return frame
    
# Prints the current game board state
def buildMap (gameMap):
    frame = getFrame(gameMap.map_size)
    legend = getLegend(gameMap.map_size)

    print('\nHuman: O  | Comp 2: X')
    print(frame)
    for row in gameMap.map_state:
        for column in row:
            print('|', end=' ')

            symbol = ''
            if column == -1: symbol = ' '
            if column ==  0: symbol = 'O'
            if column ==  1: symbol = 'X'

            print(symbol, end=' ')

        print('|')
        print(frame)
    print(legend)

    return

#Returns true if the selected column slot is available
def checkSlot (gameMap, slot):
    open_spot = 0
    for i in range(gameMap.map_size):
        current_token = gameMap.map_state[i][slot-1]
        if current_token == -1:
            open_spot = open_spot + 1

    if open_spot > 0:
        return True
    else:
        return False


#Returns true if the selected column slot is available
# def checkSlot (gameMap, slot):
    # open_spot = 0
    # for i in range(gameMap.map_size):
        # current_token = gameMap.map_state[i][slot-1]
        # if current_token == -1:
            # return True
    # return False

#Updates the board with a given move slot
def updateMap (gameMap, slot, symbol):
    for i in range(gameMap.map_size):
        current_token = gameMap.map_state[i][slot-1]
        if current_token != -1:
            gameMap.map_state[i-1][slot-1] = symbol
            return gameMap

    size = gameMap.map_size
    gameMap.map_state[size-1][slot-1] = symbol

    return gameMap
    
# Returns true if game is over
def gameOver(gameMap, matrix_size, win_length)
    inaRow = 0
    #check 0 column victory
    for row in gameMap.map_state:
        inaRow = 0
        for column in row:
            if column == 0:
                inaRow += 1
                if inaRow == win_length
                return true
    
