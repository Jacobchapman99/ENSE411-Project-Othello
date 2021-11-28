import OthelloRefined
import OthelloStrategiesRefined

def main():
    print("Welcome to the game of Othello")
    
    black, white = getPlayers()
    gameBoard, score = OthelloRefined.playGame(black, white)

    print("final score: ", score)
    if score > 0:
        print("Black wins")
    else:
        print("White wins")
    
    print(OthelloRefined.printGameBoard(gameBoard))


# Checks the players move to see if it is a legal one
def checkMove(move, player, gameBoard):
    return OthelloRefined.moveIsValidRefined(move) and OthelloRefined.isLegal(move, player, gameBoard)


# Defines the human user
def humanPlayer(player, board):
    print(OthelloRefined.printGameBoard(board))
    print("Your move")

    while(True):
        move = int(input("> ")) # gets player input

        if move and checkMove(move, player, board):
            return move
        elif move:
            print("That move is illegal. Try again.")


# provides user with a list of options to choose from, for the play strategy
def getOptions(prompt, options):
    print(prompt)
    print("Options: ", options.keys())

    while(True):
        choice = input("> ") # gets user input

        if choice in options:
            return options[choice]
        elif choice:
            print("Invalid option")


def getPlayers():
    print("Welcome to the game of Othello")
    
    optionsList = {"human": humanPlayer, 
                   
                   # Random AI
                   "random": OthelloStrategiesRefined.getRandom,
                   
                   # MiniMax AI
                   "minimax-trivial": OthelloStrategiesRefined.minimaxSearcher(2, OthelloStrategiesRefined.coinParityHeuristic),
                   "minimax-beginner": OthelloStrategiesRefined.minimaxSearcher(2, OthelloStrategiesRefined.stabilityHeuristic),
                   "minimax-amateur": OthelloStrategiesRefined.minimaxSearcher(2, OthelloStrategiesRefined.mobilityHeuristic), # depth of 3 = max. any deeper will cause too high of runtime for it to run
                   "minimax-intermediate": OthelloStrategiesRefined.minimaxSearcher(3, OthelloStrategiesRefined.intermediateHeuristic),
                   
                   # Alpha-Beta AI
                   "alpha-beta-trivial": OthelloStrategiesRefined.alphaBetaSearcher(2, OthelloStrategiesRefined.coinParityHeuristic),
                   "alpha-beta-beginner": OthelloStrategiesRefined.alphaBetaSearcher(2, OthelloStrategiesRefined.stabilityHeuristic),
                   "alpha-beta-amateur": OthelloStrategiesRefined.alphaBetaSearcher(2, OthelloStrategiesRefined.mobilityHeuristic),
                   "alpha-beta-intermediate": OthelloStrategiesRefined.alphaBetaSearcher(3, OthelloStrategiesRefined.intermediateHeuristic)
                   
                   # Expectimax
                   
                   }
    
    # Instantiates both players. They could both be AI's, or both humans, or one human and one AI
    # Black = x
    # White = o
    black = getOptions("BLACK: choose an option", optionsList) 
    white = getOptions("WHITE: choose an option", optionsList)

    return black, white


# Runs the Othello game
if __name__ == "__main__":
    main()