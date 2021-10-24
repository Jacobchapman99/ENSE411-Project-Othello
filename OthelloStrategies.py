import Othello
import random

heuristic = [
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0, 200,  40,  20,  10,  10,  20,  40, 200,   0,
    0,  40,  80,  10,  10,  10,  10,  80,  40,   0,
    0,  20,  10,  40,   6,   6,  40,  10,  20,   0,
    0,  10,  10,   6,   6,   6,   6,  10,  10,   0,
    0,  10,  10,   6,   6,   6,   6,  10,  10,   0,
    0,  20,  10,  40,   6,   6,  40,  10,  20,   0,
    0,  40,  80,  10,  10,  10,  10,  80,  40,   0,
    0, 200,  40,  20,  10,  10,  20,  40, 200,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
]

# Random Strategy. Easiest form where moves are picked at random
def getRandom(player, board):
    return random.choice(Othello.legalMoves(player, board))


# IMPLEMENT: Minimax Search

# IMPLEMENT: Alpha-Beta Search



    


