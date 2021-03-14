import sys

import numpy as np
from data.map import Map
import gameState as gs

    #takes in the current board state and returns a slot that is the move choice
def alphBetSearch(gameMap):\
    #Generate entire game tree up to a certain depth
    #apply utility function to the leaves
    #Propagate upwards to the root (max nodes receiving the max of their children and the opposite for min nodes)
    #Return the move slot of the child with the highest value in the end
    return


#takes in a board state and returns a value that represents how favorable it is. 
def evaluateStateValue(gameMap):
    # Could be just like the gameOver function but look for 2, 3, up to win_length - 1 in a row
    # Add a value to the state's value based on how many of the above options there are in a row
    # (Possibly 1pt for 2, 2pts for 3, etc.) And subtr
    #
    return