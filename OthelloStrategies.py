import Othello
import random

heuristic = [
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0, 120, -20,  20,   5,   5,  20, -20, 120,   0,
    0, -20, -40,  -5,  -5,  -5,  -5, -40, -20,   0,
    0,  20,  -5,  15,   3,   3,  15,  -5,  20,   0,
    0,   5,  -5,   3,   3,   3,   3,  -5,   5,   0,
    0,   5,  -5,   3,   3,   3,   3,  -5,   5,   0,
    0,  20,  -5,  15,   3,   3,  15,  -5,  20,   0,
    0, -20, -40,  -5,  -5,  -5,  -5, -40, -20,   0,
    0, 120, -20,  20,   5,   5,  20, -20, 120,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
]

##################
# 1: Random Search
##################

# Random Strategy. Easiest form where moves are picked at random
def getRandom(player, board):
    return random.choice(Othello.legalMoves(player, board))


######################################################################
# 2: Minimax Search
# description: very affective, however it expands too many nodes. 
#              The branching factor for Othello is 10, and evaluates
#              many search trees that can be ignored.
######################################################################

# find the best legal move for the player by searching to a specific depth
# returns a tuple (move, minimum score)
def minimax(player, gameBoard, depth, evaluate):

    # define the value of the gameBoard to be opposite of its value for our opponent. 
    # recursively goes through minimax for the opponent
    def value(gameBoard):
        return -minimax(Othello.getOpponent(player), gameBoard, depth - 1, evaluate)[0]

    # if the depth is 0, dont look at any more potential moves, simply determine the value of the gameBoard for this player
    if depth == 0:
        return evaluate(player, gameBoard), None


    moves = Othello.legalMoves(player, gameBoard) # want to evaluate all legal moves by looking at implications 
    legalmoves = Othello.anyLegalMove(Othello.getOpponent(player), gameBoard)

    if not moves: # if player has no legal moves, then 
        if not legalmoves: # the game is over, so return the final score
            return finalValue(player, gameBoard), None
        
        # or there has to be a pass of a turn, so determine score of this gameBoard
        return value(gameBoard), None 
    
    # return the best possible move by maximizing the value of the resulting boards
    return max((value(Othello.makeMove(move, player, list(gameBoard))), move) for move in moves)

maxValue = sum(map(abs, heuristic))
minValue = -maxValue

# End game situation where the final score is returned
def finalValue(player, gameBoard):

    score = Othello.score(player, gameBoard)
    if score < 0:
        return minValue
    elif score > 0:
        return maxValue
    return score

# strategy function that uses the minimax function. Called in main()
def minimaxSearcher(depth, evaluate):

    def strategy(player, gameBoard):
        return minimax(player, gameBoard, depth, evaluate)[1]
    return strategy

        

        
# IMPLEMENT: Alpha-Beta Search



    


