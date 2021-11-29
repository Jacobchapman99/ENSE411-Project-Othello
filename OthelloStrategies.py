import Othello
import OthelloGame
import random

# base Heuristic 
def baseHeuristic():
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
    return heuristic
    
# Coin Parity heuristic (analagous to greedy search)
def coinParityHeuristic(player, gameBoard):
    blackCoins = 0
    whiteCoins = 0
    valueX = 'x'
    valueO = 'o'

    #for square in gameBoard:
        #if square == valueX:
            #blackCoins += 1
        #if square == valueO:
            #whiteCoins += 1
            
    for square in Othello.squares():
        piece = gameBoard[square]
        if piece == player:
            blackCoins += 1
        elif piece == Othello.getOpponent(player):
            whiteCoins += 1
            
    coinParity = 0
    
    if player == valueX:
        coinParity = 100 * ((blackCoins - whiteCoins) / (blackCoins + whiteCoins))
    elif player == valueO:
        coinParity =  100 * ((whiteCoins - blackCoins) / (blackCoins + whiteCoins))
    
    return coinParity


# A heuristic based on the difference in legal moves between the max player and min player
def mobilityHeuristic(player, gameBoard):
    playerMobility = 0
    opponentMobility = 0
    
    opponent = "White" if player == "Black" else "Black"
    
    for square in Othello.squares():
        if OthelloGame.checkMove(square, player, gameBoard):
            playerMobility += 1
        elif OthelloGame.checkMove(square, opponent, gameBoard):
            opponentMobility += 1
    
    if (playerMobility + opponentMobility) != 0:
        return 100 * (playerMobility - opponentMobility) / (playerMobility + opponentMobility)
    else:
        return 0

# A heuristic that combines coin parity and mobility
def intermediateHeuristic(player, gameBoard):
    return coinParityHeuristic(player, gameBoard) + mobilityHeuristic(player, gameBoard)
 
# Could possibly extend with with POTENTIAL MOBILITY (i.e. moves that may become legal after the opponent's next move)
# Maybe a refined breadth-first search could be applicable here?


# Corner heuristic 
def cornerHeuristic(player, gameBoard):
    return

# Stability heuristic
# stable coins: cannot be flanked 
# unstable coins: can be flanked next turn (i.e moves) 
# semi-stable coins: can be flanked in the future, but not this turn
def stabilityHeuristic(player, gameBoard):
    
    playerMoves = Othello.legalMoves(player, gameBoard) # unstable coins (given a -1 for each coin that can be flanked)
    opponentMoves = Othello.legalMoves(Othello.getOpponent(player), gameBoard)
    playerPieces = 0
    opponentPieces = 0
    
    # check each square and add 1
    for square in Othello.squares():
        piece = gameBoard[square]
        if piece == player:
            playerPieces += 1
        elif piece == Othello.getOpponent(player):
            opponentPieces += 1
            
    playerStability = playerPieces - len(playerMoves) 
    opponentStability = opponentPieces - len(opponentMoves)
    
    if((playerStability + opponentStability) != 0):
        return 100 * ((playerStability - opponentStability) / (playerStability + opponentStability))
    else:
        return 0
    
##################
# 1: Random Search
##################

# Random Strategy. Easiest form where moves are picked at random
def getRandom(player, gameBoard):
    return random.choice(Othello.legalMoves(player, gameBoard))


######################################################################
# 2: Minimax Search
# description: very affective, however it expands too many nodes. 
#              The branching factor for Othello is 10, and evaluates
#              many search trees that can be ignored.
######################################################################

# find the best legal move for the player by searching to a specific depth
# returns a tuple (move, minimum score)
def minimax(player, gameBoard, depth, evaluate):
    # define the value of the gameBoard to be opposite of its value for our opponent. recursively goes through minimax for the opponent
    def value(gameBoard):
        return -minimax(Othello.getOpponent(player), gameBoard, depth - 1, evaluate)[0]

    # if the depth is 0, dont look at any more potential moves, simply determine the value of the gameBoard for this player
    if depth == 0:
        return evaluate(player, gameBoard), None

    moves = Othello.legalMoves(player, gameBoard)
    legalmoves = Othello.anyLegalMove(Othello.getOpponent(player), gameBoard)

    # if player has no legal moves, then the game is over, so return the final score. Or there has to be a pass of a turn, so determine score of this gameBoard
    if not moves: 
        if not legalmoves: 
            return finalValue(player, gameBoard), None
        return value(gameBoard), None 
    
    # return the best possible move by maximizing the value of the resulting boards
    return max((value(Othello.makeMove(move, player, list(gameBoard))), move) for move in moves)


maxValue = sum(map(abs, baseHeuristic()))
minValue = -maxValue
 
# strategy function that uses the minimax function. Called in main()
def minimaxSearcher(depth, evaluate):
    def strategy(player, gameBoard):
        return minimax(player, gameBoard, depth, evaluate)[1]
    return strategy

        

######################  
# 3: Alpha-Beta Search
######################

# find the best legal move for the player by searching to a specific depth however uses alpha and beta pruning technique
def alphaBeta(player, gameBoard, alpha, beta, depth, evaluate):

    if depth == 0:
        return (evaluate(player, gameBoard), None)
    
    # similar to minimax
    # -alpha : the best score for us, therefore the worst score for opponent.
    # -beta : the worst score for us, therefore the best score for opponent.
    def value(gameBoard, alpha, beta):
        return -alphaBeta(Othello.getOpponent(player), gameBoard, -alpha, -beta, depth - 1, evaluate)[0]

    moves = Othello.legalMoves(player, gameBoard)
    anylegalMove = Othello.anyLegalMove(Othello.getOpponent(player), gameBoard)
    if not moves:
        if not anylegalMove:
            return (finalValue(player, gameBoard), None)
        return (value(gameBoard, alpha, beta), None)
    
    optimalMove = moves[0]
    for move in moves:
        
        # if a legal move is possible that makes a better score than beta, then opponent will avoid branching here (quit looking)
        if alpha >= beta:
            break
        
        v = value(Othello.makeMove(move, player, list(gameBoard)), alpha, beta)

        if v > alpha:
            alpha = v
            optimalMove = move
    
    return (alpha, optimalMove)

def alphaBetaSearcher(depth, evaluate):
    def strategy(player, gameBoard):
        return alphaBeta(player, gameBoard, minValue, maxValue, depth, evaluate)[1]
    return strategy


######################  
# 4: Expectimax Search
######################
def expectimax(player, gameBoard, depth, evaluate): # Needs to be implemented
    return 0
    

def expectimaxSearcher(depth, evaluate):
    def strategy(player, gameBoard):
        return expectimax(player, gameBoard, depth, evaluate)
    return strategy




# End game situation where the final score is returned
def finalValue(player, gameBoard):
    score = Othello.score(player, gameBoard)
    if score < 0:
        return maxValue
    elif score > 0:
        return minValue
    return score
