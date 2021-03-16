import sys

import numpy as np
from data.map import Map
import gameState as gs
from data.node import Node

#set the depth to search here
depth = 3
infinity = 999999999

# m is the matrix size
# w is the win_length
# s is the player symbol
def alphBetSearch(gameMap, m, w, s):

    best_score = -infinity
    best_slot = None

    for slot in range(m):
        if gs.checkSlot(gameMap, slot):
            tempMap = gameMap
            tempMap = gs.updateMap(tempMap, slot, s)

            score = minMaxSearch(tempMap, depth, True, m, w, s)
            if score > best_score:
                best_score = score
                best_slot = slot 
    return best_slot

def minMaxSearch (gameMap, depth, isMax, m, w, s):
    isOver = gs.gameOver(gameMap, m, w, s)
    if isOver == 1 or depth == 0:
        return 

    if isMax:
        best_score = -infinity
        for slot in range(m):
            if gs.checkSlot(gameMap, slot):
                tempMap = gameMap
                tempMap = gs.updateMap(tempMap, slot, s)

                score = minMaxSearch(tempMap, depth-1, False, m, w, 0)
                if score > best_score:
                    best_score = score
        return best_score

    else:
        best_score = infinity
        for slot in range(m):
            if gs.checkSlot(gameMap, slot):
                tempMap = gameMap
                tempMap = gs.updateMap(tempMap, slot, s)

                score = minMaxSearch(tempMap, depth-1, True, m, w, 1)
                if best_score > score:
                    best_score = score
        return best_score
        

    #returns the net value of a game state
def evaluateStateValue(gameMap, win_length, matrix_size, currPlayerSymbol):
    otherSymbol = 0
    if currPlayerSymbol == 0:
        otherSymbol = 1
    return evaluate(gameMap, win_length, matrix_size, currPlayerSymbol) - evaluate(gameMap, win_length, matrix_size, otherSymbol)

#takes in a board state and returns a value that represents how favorable it is. 
def evaluate(gameMap, win_length, matrix_size, currPlayerSymbol):
    # Could be just like the gameOver function but look for 2, 3, up to win_length - 1 in a row (with an empty slot available still) <- doesnt do that last part yet
    # Add a value to the state's value based on how many of the above options there are in a row
    # (Possibly 1pt for 2, 2pts for 3, etc.) And subtract the same value for the opponent 
    # return the net value
    stateScore = 0
    inaRow = 0
    #setting the opponent's Symbol
    opponentSymbol = 0
    if currPlayerSymbol == 0:
        opponentSymbol = 1

    #check for 0 row victory
    for row in gameMap.map_state:
        inaRow = 0
        for column in row:
            if column == currPlayerSymbol:
                inaRow += 1
                if inaRow >= 1:
                    #only need to add 1 each time, since this will happen for each slot counted as being in a row
                    stateScore += 1
                if inaRow == win_length: return 1
            else:
                inaRow = 0

    #check 0 column victory
    for x in range(matrix_size):
        inaRow = 0
        for column in gameMap.map_state:
            if column[x] == currPlayerSymbol:
                inaRow += 1
                if inaRow > 1:
                    #only need to add 1 each time, since this will happen for each slot counted as being in a row
                    stateScore += 1
                if inaRow == win_length: return 1
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
                    if positive_diagonal_count > 1:
                        stateScore += 1

                current_negative_symbol = gameMap.map_state[i + count][j + count]
                if current_negative_symbol == negative_diagonal_symbol:
                    negative_diagonal_count = negative_diagonal_count + 1
                    if negative_diagonal_count > 1:
                        stateScore += 1
    return   stateScore


#Returns true if a node is below desired depth limit
def cutoffTest(node):
    depthCount = 0
    nodePtr = node
    while(nodePtr.hasParent()):
        nodePtr = nodePtr.get_parent()
        depthCount += 1
        if depthCount > depth:
            return True
    return False