import gameState as gs
import sys

import numpy as np

from data.map import Map

gameMap = Map()

# Returns true if a valid first move parameter has been given
def validatePlayer (first_move):
    if first_move == 0 or first_move == 1:
        return True

    return False
    
# Returns true if the imput parameters are valid
def validateGame (m_size, win_length, first_move):
    if m_size >= 3 and m_size <= 10:
        if win_length >= 1 and win_length <= m_size:
            playerMove = validatePlayer(first_move)

            if playerMove:
                return True
            else:
                print('First player could not be determined')
                return False  
        else:
            print('Win condition is impossible')
            return False
  
    print('Matrix size should be between 3 and 10')
    return False

def winCondition (gameMap, matrix_size, win_length, currPlayerSymbol):
    isOver = gs.gameOver(gameMap, matrix_size, win_length, currPlayerSymbol)

    if isOver > 0: 
        print('\nGame Over! The ' + gameMap.winner + ' won this time!')
        sys.exit()

    if isOver == 0:
        print('\nGame ends in a draw!')
        sys.exit()
    
    print('No one has won yet')
    return

def main (argv):
    matrix_size = int(argv[0])
    win_length = int(argv[1])
    first_move = int(argv[2])

    game = validateGame(matrix_size, win_length, first_move)

    if game:
        gameMap = gs.startState(matrix_size)
        gs.buildMap(gameMap)
        playerMove = first_move == 0
        
        while True:
            if playerMove:
                while True: 
                    input_text = input('[Choose a slot (1-' + str(matrix_size) + ')]: ')
                    if input_text == '':
                        return
                    
                    player_input = int(input_text)
                    if player_input >= 0 or player_input <= matrix_size:
                        validSlot = gs.checkSlot(gameMap, player_input)
                        if validSlot:
                            break
                    
                    print(str(player_input) + ' is not a valid slot')

                gameMap = gs.updateMap(gameMap, player_input, 0)
                gs.buildMap(gameMap)
                # gameOver is checked after AI move and after player move | 0 FOR AI
                winCondition(gameMap, matrix_size, win_length , 0)
            
            print('ai does some crazy stuff and makes a move')
            #this is where you would call min max analysis
            #followed by the ai's percieved optimal move
            #gameMap = gs.updateMap(gameMap, agent_input, 1)
            # winCondition is checked after AI move and after player move | 1 FOR PLAYER
            winCondition(gameMap, matrix_size, win_length , 1)
            gs.buildMap(gameMap)
            playerMove = True


if __name__ == '__main__':
    main(sys.argv[1:])