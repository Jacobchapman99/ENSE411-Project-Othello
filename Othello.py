
import OthelloStrategies 
import random
####################################
#
# Part 0: Initilization of Othello
#
####################################


# Instantiate game board, and player pieces
# Black = x
# White = o
empty, black, white, outerTile = ".", "x", "o", "#"
gamePieces = (empty, black, white, outerTile)
players = {black: "Black", white: "White"}


# instantiate all directions, and arbitrary costs for moving.
north, south, west, east = -10, 10, -1, 1
northEast, southEast, southWest, northWest = -9, 11, 9, -11
directions = (north, northEast, east, southEast, south, southWest, west, northWest)


# Defines a list of all the available squares on the game board
def squares():
    return [i for i in range(11, 89) if 1 <= (i % 10) <= 8]

def corners():
    return [11, 18, 81, 88]

def board_init():

    gameBoard = [outerTile] * 100

    # instantiate board to empty spaces
    for square in squares():
        gameBoard[square] = empty
    
    # start with players in the center of the game board
    gameBoard[44], gameBoard[45] = white, black
    gameBoard[54], gameBoard[55] = black, white

    return gameBoard


def printGameBoard(gameBoard):

    gameBoardStr = ""
    gameBoardStr += "  %s\n" % " ".join(map(str, ['a','b','c','d','e','f','g','h']))

    # iterates through each row of numbers. range is a just a list of numbers that get iterated through.
    # In our case, we want 1 through 9 rows to instantiate
    for row in range(1,9):
        start, end = (10 * row + 1), (10 * row + 9)
        gameBoardStr += '%d %s\n' % (row, ' '.join(gameBoard[start:end]))
    
    return gameBoardStr



#################################
# 
# Part 1: Check player moves
#
#################################

# Checks if the move being played is on the board
def moveIsValid(move):
    # returns whether or not the player makes a move in a proper location (sqaure)
    return isinstance(move, int) and move in squares()

# Gets the opponent players piece
def getOpponent(player):

    if player is not black:
        return black
    else:
        return white


# Find a square that creates a bracket with "square" for that player in the
# given direction. 
def findSqaureWithBracket(square, player, gameBoard, direction):

    bracket = square + direction

    if gameBoard[bracket] == player:
        return None

    opponent = getOpponent(player)

    while gameBoard[bracket] == opponent:
        bracket += direction

    if gameBoard[bracket] in (outerTile, empty):
        return None
    else:
        return bracket


# Is this move a legal one for that player
def isLegal(move, player, gameBoard):

    hasBracket = lambda direction : findSqaureWithBracket(move, player, gameBoard, direction)
    return gameBoard[move] == empty and any(map(hasBracket, directions))


##############################################################
# 
# Part 2: Making player moves. 
# 
# Functionality: When a player makes
#                a move, we need to update the board and flip
#                all the bracketed pieces
#
#############################################################

def makeMove(move, player, gameBoard):

    gameBoard[move] = player

    for d in directions:
        flipOpponentPieces(move, player, gameBoard, d)

    return gameBoard


def flipOpponentPieces(move, player, gameBoard, direction):

    bracket = findSqaureWithBracket(move, player, gameBoard, direction)

    if not bracket:
        return None

    square = move + direction

    while square != bracket:
        gameBoard[square] = player
        square += direction


#################################
# 
# Part 3: Monitor players
#
#################################

class IllegalMoves(Exception):

    def __init__(self, player, move, gameBoard):
        self.player = player
        self.move = move
        self.gameBoard = gameBoard

    def __str__(self):
        return '%s cannot move to that location %d' % (players[self.player], self.move)


# returns a list of all the legal moves available
def legalMoves(player, gameBoard):
    return [square for square in squares() if isLegal(square, player, gameBoard)]

def legalMovesLength(player, gameBoard):
    length = 0
    for square in squares():
        if isLegal(square, player, gameBoard):
            length += 1
    return length
            
            
# returns if the player can make any move
def anyLegalMove(player, gameBoard):
    return any(isLegal(square, player, gameBoard) for square in squares())
    

##########################################################
# 
# Part 4: Playing the game
#
# Functionality: Each 'round' consists of getting a move
#                from the current player and apply it to
#                the board. Then switch players
#
#########################################################


# Plays the game of Othello and returns the final board and score
def playGame(blackStrategy, whiteStrategy):

    gameBoard = board_init()
    player = black

    # lamda in python is just a command line function -> lambda args : function code
    strategy = lambda who : blackStrategy if who == black else whiteStrategy
    numMoves = 4
    while player is not None:
        # implement 4 random moves to start, then go to the strategy
        # FOR TESTING N GAMES
        while numMoves > 0:
            move = random.choice(legalMoves(player, gameBoard))
            makeMove(move, player, gameBoard)
            player = nextPlayer(gameBoard, player)
            numMoves -= 1
        
        move = getMove(strategy(player), player, gameBoard)
        makeMove(move, player, gameBoard)
        player = nextPlayer(gameBoard, player)

    return gameBoard, score(black, gameBoard)

# gets the next player to make a move. Returns none if no legal moves are available
def nextPlayer(gameBoard, prevPlayer):

    opponent = getOpponent(prevPlayer)

    if anyLegalMove(opponent, gameBoard):
        return opponent
    elif anyLegalMove(prevPlayer, gameBoard):
        return prevPlayer

    return None


# calls the strategy function to obtain a move
def getMove(strategy, player, gameBoard):

    copy = list(gameBoard) # get a copy of the board

    move = strategy(player, copy)

    if not moveIsValid(move) or not isLegal(move, player, gameBoard):
        raise IllegalMoves(player, move, copy)
    
    return move

# collects each players score (number of player pieces - number of opponent pices)
def score(player, gameBoard):
    myScore, theirScore = 0, 0
    opponent = getOpponent(player)

    for square in squares():
        piece = gameBoard[square]
        if piece == player:
            myScore += 1
        elif piece == opponent:
            theirScore += 1
    
    return myScore - theirScore



