import Othello
import OthelloStrategies

def main():
    black, white = getPlayers()
    gameBoard, score = Othello.playGame(black, white)

    print("final score: ", score)
    if score > 0:
        print("Black wins")
    else:
        print("White wins")
        
    print(Othello.printGameBoard(gameBoard))


# Checks the players move to see if it is a legal one
def checkMove(move, player, gameBoard):
    return Othello.moveIsValid(move) and Othello.isLegal(move, player, gameBoard)


# Defines the human user
def humanPlayer(player, board):
    print(Othello.printGameBoard(board))
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
                   "random": OthelloStrategies.getRandom,
                   "minimax-beginner": OthelloStrategies.minimaxSearcher(2, OthelloStrategies.coinParityHeuristic),
                   "minimax-amateur": OthelloStrategies.minimaxSearcher(2, OthelloStrategies.mobilityHeuristic), # depth of 3. any deeper will cause too high of runtime for it to run
                   "minimax-intermediate": OthelloStrategies.minimaxSearcher(3, OthelloStrategies.intermediateHeuristic),
                   "alpha-beta-beginner": OthelloStrategies.alphaBetaSearcher(2, OthelloStrategies.coinParityHeuristic),
                   "alpha-beta-amateur": OthelloStrategies.alphaBetaSearcher(2, OthelloStrategies.mobilityHeuristic),
                   "alpha-beta-intermediate": OthelloStrategies.alphaBetaSearcher(3, OthelloStrategies.intermediateHeuristic)
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
