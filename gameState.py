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
    if slot < 1 or slot > gameMap.map_size:
        return False
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

def setWinner (gameMap, symbol):
    if symbol == 0:
        gameMap.winner = 'HUMAN'
    else:
        gameMap.winner = 'COMPUTER'
  
# Exits and prints ending message if game is over
def gameOver(gameMap, matrix_size, win_length, currPlayerSymbol):
    inaRow = 0
    #check for 0 row victory
    for row in gameMap.map_state:
        inaRow = 0
        for column in row:
            if column == currPlayerSymbol:
                inaRow += 1
                if inaRow == win_length: 
                    setWinner(gameMap, currPlayerSymbol)
                    return 1
            else:
                inaRow = 0

    #check 0 column victory
    for x in range(matrix_size):
        inaRow = 0
        for column in gameMap.map_state:
            if column[x] == currPlayerSymbol:
                inaRow += 1
                if inaRow == win_length: 
                    setWinner(gameMap, currPlayerSymbol)
                    return 1
            else:
                inaRow = 0

    #Testloop for diagonal left to right
    index_diff = matrix_size - win_length + 1
    map_size = matrix_size - 1

    for i in range(index_diff):
        for j in range(index_diff):
            positive_diagonal_symbol = gameMap.map_state[map_size - i][j]
            positive_diagonal_count = 0

            negative_diagonal_symbol = gameMap.map_state[i][j]
            negative_diagonal_count = 0

            for count in range(win_length):
                current_positive_symbol = gameMap.map_state[map_size - i - count][j + count]
                if current_positive_symbol == positive_diagonal_symbol:
                    positive_diagonal_count = positive_diagonal_count + 1

                current_negative_symbol = gameMap.map_state[i + count][j + count]
                if current_negative_symbol == negative_diagonal_symbol:
                    negative_diagonal_count = negative_diagonal_count + 1
                    
            if positive_diagonal_count == win_length:
                if current_positive_symbol == -1: continue
                setWinner(gameMap, positive_diagonal_symbol)
                return 1

            if negative_diagonal_count == win_length:
                if current_negative_symbol == -1: continue
                setWinner(gameMap, negative_diagonal_symbol)
                return 1

    return -1

