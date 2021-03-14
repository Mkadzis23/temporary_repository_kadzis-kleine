import sys

import numpy as np
from data.map import Map
import gameState as gs

    #takes in the current board state and returns a slot that is the move choice
def alphBetSearch(gameMap):
    return
#takes in a board state and returns a value that represents how favorable it is. Terminal states should be +inf, and loses should be -inf
def evaluateStateValue(gameMap):
    # Could be just like the gameOver function but look for 2, 3, up to win_length - 1 in a row
    # Add a value to the state's value based on how many of the above options there are in a row
    # (Possibly 1pt for 2, 2pts for 3, etc.) And subtr
    #
    return