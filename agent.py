import sys

import numpy as np
from data.map import Map
import gameState as gs
from data.node import Node

#set the depth to search here
depth = 5
posInf = 999999999
negInf = -999999999
    #takes in the current board state and returns a slot that is the move choice
def alphBetSearch(gameMap, currPlayerSymbol, matrix_size, win_length):
    alpha = negInf
    beta = posInf
    a = None
    moves = None
    node =  Node(gameMap)
    for slot in range(matrix_size):
        if(gs.checkSlot(gameMap, slot)):
            moves.append(slot) 
            #alphaPrime = minValue(node, 
            #make tree for that slot
        else:
            #Reached leaf, so call utility func
             return evaluateStateValue(gameMap, win_length, matrix_size, currPlayerSymbol)
    
    
    
    #should the map have an associated node or something?
    def minValue(node, gameMap, alpha, beta):
        depthCount = 0
        validMoves = []
        for slot in range(gameMap.map_size):
            if (gs.checkSlot(gameMap, slot)):
                tempMap = gs.updateMap(gameMap, slot, currPlayerSymbol)
                validMoves.append(tempMap)
        if len(validMoves) == 0 or cutoffTest(node):
            return evaluateStateValue(gameMap, win_length, matrix_size, currPlayerSymbol)
        
        #reassigning validMoves to the actual slots rather than the states
        validMoves = None
        for slot in range(gameMap.map_size):
            if (gs.checkSlot(gameMap, slot)):
                validMoves.append(slot)
        #for(slot in validMoves):
        
       
   #board depth max min playersymbol



    #Generate entire game tree up to a certain depth
    #apply utility function to the leaves
    #Propagate upwards to the root (max nodes receiving the max of their children and the opposite for min nodes)
    #Return the move slot of the child with the highest value in the end
    return


#takes in a board state and returns a value that represents how favorable it is. 
def evaluateStateValue(gameMap, win_length, matrix_size, currPlayerSymbol):
    # Could be just like the gameOver function but look for 2, 3, up to win_length - 1 in a row (with an empty slot available still) <- doesnt do that last part yet
    # Add a value to the state's value based on how many of the above options there are in a row
    # (Possibly 1pt for 2, 2pts for 3, etc.) And subtract the same value for the opponent 
    # return the net value
    stateScore = 0
    inaRow = 0

    #####FOR CURRENT PLAYER

    #check for 0 row victory
    for row in gameMap.map_state:
        inaRow = 0
        for column in row:
            if column == currPlayerSymbol:
                inaRow += 1
                if inaRow > 1:
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
   
   
    #####FOR 'ENEMY' PLAYER
    if currPlayerSymbol == 0:
        currPlayerSymbol = 1
    else:
        currPlayerSymbol = 0
    for row in gameMap.map_state:
        inaRow = 0
        for column in row:
            if column == currPlayerSymbol:
                inaRow += 1
                if inaRow > 1:
                    #only need to subtract 1 each time, since this will happen for each slot counted as being in a row
                    stateScore -= 1
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
                    #only need to subtract 1 each time, since this will happen for each slot counted as being in a row
                    stateScore -= 1
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
                        stateScore -= 1

                current_negative_symbol = gameMap.map_state[i + count][j + count]
                if current_negative_symbol == negative_diagonal_symbol:
                    negative_diagonal_count = negative_diagonal_count + 1
                    if negative_diagonal_count > 1:
                        stateScore -= 1
    #print(stateScore)
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