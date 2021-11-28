# Othello
Othello (also known as Reversi) is a 2-player board game played on an 8x8 uncheckered board. 
There are 64 spaces that can be occupied, and each player starts in the middle of the game board 
with 2 discs (black and white) opposite of one another. Players take turns placing their discs 
on the board with their assigned color. During a players turn, any discs of the opponents color
that are either in a **straight line** and **bounded** by the current players disc that was just placed
are turned over. The objective of the game is to have the majority of the discs on the board. The game
ends when all spaces are filled or when the player has no playable moves available.

## Game Setup
The game is ran when 2 players choose who they are. There can be human-to-human, human-to-Computer,
or computer-to-computer games. 

## AI Algorithms 
In our implementation of Othello (referenced from Peter Norvig's textbook, "Paradigms of Artificial 
Intelligence"), we used random, MiniMax, and Alpha-Beta pruning strategies for the computer players. 
The computer players can use optimal heuristics, or sub-par heurstics (respective to easy, medium,
and hard difficulties). 

## Evaluation Functions
We implemented 4 different heuristics (static weights, Coin Parity, Stability, Mobility, and a combination of coin parity and mobility) as described in Vaishnavi Sannidhanam and Muthukaruppan Annamalai academic paper "An Analysis of Heuristics in Othello". 



