import board as b 
import pieces as p 
import utility as u 
import game as g 
import heapq

#Transposition Table and iteritive deepening 
#Game table for each peice thats adds or subtracts value based on piece position 

def alpha_prune(board, turn, color, depth, alpha, beta):
    if depth == 0 or is_leaf_node():
        g.evaluate(board)
    while turn == True:
        max_eval = float("-inf")
        for move in u.possible_moves(board, color):
            new_board = u.apply_move(board, move[2], move[3])
            eval = alpha_prune(new_board, False, color, depth - 1, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
        if beta <= alpha:
                break
        return max_eval
    while turn == False:
        min_eval = float("inf")
        new_board = u.apply_move(board, move[2], move[3])
        eval = alpha_prune(board, True, color, depth - 1, alpha, beta)
        min_eval = min(min_eval, eval)
        beta = min(beta, eval)
        if beta <= alpha:
                break
        return max_eval


def is_leaf_node(board,depth):
     #checkmate, stalemate, not enought material to win
    
    
        

