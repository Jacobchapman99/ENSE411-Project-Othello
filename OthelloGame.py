import Othello
import OthelloStrategies 

def main():
    print("Welcome to the game of Othello!")
    print("Do you wish to play a sequence of games, or a single game? (Enter 1 for  sequence, 0 for single)")
    choice = int(input("> "))
    
    if choice == 1:
        print("How many games do you wish to play?")
        numGamesTotal = int(input("> "))
        numGames = numGamesTotal
        
        blackGamesWon = 0
        whiteGamesWon = 0
        blackCoinsCaptured = 0
        whiteCoinsCaptured = 0
        
        while numGames > 0:
            #black = OthelloStrategies.getRandom
            
            #black = OthelloStrategies.minimaxSearcher(2, OthelloStrategies.coinParityHeuristic)
            #black = OthelloStrategies.minimaxSearcher(2, OthelloStrategies.stabilityHeuristic)
            #black = OthelloStrategies.minimaxSearcher(2, OthelloStrategies.mobilityHeuristic)
            #black = OthelloStrategies.minimaxSearcher(2, OthelloStrategies.intermediateHeuristic)
            
            #black = OthelloStrategies.alphaBetaSearcher(2, OthelloStrategies.coinParityHeuristic)
            #black = OthelloStrategies.alphaBetaSearcher(2, OthelloStrategies.stabilityHeuristic)
            #black = OthelloStrategies.alphaBetaSearcher(2, OthelloStrategies.mobilityHeuristic)
            black = OthelloStrategies.alphaBetaSearcher(2, OthelloStrategies.intermediateHeuristic)
            
            #white = OthelloStrategies.getRandom
            #white = OthelloStrategies.minimaxSearcher(2, OthelloStrategies.coinParityHeuristic)
            #white = OthelloStrategies.minimaxSearcher(2, OthelloStrategies.stabilityHeuristic)
            #white = OthelloStrategies.minimaxSearcher(2, OthelloStrategies.mobilityHeuristic)
            #white = OthelloStrategies.minimaxSearcher(2, OthelloStrategies.intermediateHeuristic)
            
            #white = OthelloStrategies.alphaBetaSearcher(2, OthelloStrategies.coinParityHeuristic)
            #white = OthelloStrategies.alphaBetaSearcher(2, OthelloStrategies.stabilityHeuristic)
            #white = OthelloStrategies.alphaBetaSearcher(2, OthelloStrategies.mobilityHeuristic)
            white = OthelloStrategies.alphaBetaSearcher(2, OthelloStrategies.intermediateHeuristic)
            
            gameBoard, score = Othello.playGame(black, white)

            for square in Othello.squares():
                piece = gameBoard[square]
                if piece == 'x':
                    blackCoinsCaptured += 1
                elif piece == 'o':
                    whiteCoinsCaptured += 1
            
            print("final score: ", score)
            if score > 0:
                print("Black wins")
                blackGamesWon += 1
            else:
                print("White wins")
                whiteGamesWon += 1
            
            numGames -= 1
            

        print("STATS OF GAMES")
        print("black games won: " + str(blackGamesWon))
        print("black coins captured: " + str(blackCoinsCaptured))
        print("white games won: " + str(whiteGamesWon))
        print("white coins captured: " + str(whiteCoinsCaptured))

    elif choice == 0:
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
    
    optionsList = {"human": humanPlayer, 
                   
                   # Random AI
                   "random": OthelloStrategies.getRandom,
                   
                   # MiniMax AI (Max depth k = 3)
                   "minimax-trivial": OthelloStrategies.minimaxSearcher(3, OthelloStrategies.coinParityHeuristic),
                   "minimax-beginner": OthelloStrategies.minimaxSearcher(3, OthelloStrategies.stabilityHeuristic),
                   "minimax-amateur": OthelloStrategies.minimaxSearcher(3, OthelloStrategies.mobilityHeuristic), 
                   "minimax-intermediate": OthelloStrategies.minimaxSearcher(3, OthelloStrategies.intermediateHeuristic),
                   
                   # Alpha-Beta AI
                   "alpha-beta-trivial": OthelloStrategies.alphaBetaSearcher(3, OthelloStrategies.coinParityHeuristic),
                   "alpha-beta-beginner": OthelloStrategies.alphaBetaSearcher(3, OthelloStrategies.stabilityHeuristic),
                   "alpha-beta-amateur": OthelloStrategies.alphaBetaSearcher(3, OthelloStrategies.mobilityHeuristic),
                   "alpha-beta-intermediate": OthelloStrategies.alphaBetaSearcher(3, OthelloStrategies.intermediateHeuristic),
                   
                   # Expectimax
                   # "expectimax-beginner": OthelloStrategies.expectimaxSearcher(3, OthelloStrategies.coinParityHeuristic)
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