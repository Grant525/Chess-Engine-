import board as b 
import pieces as p 
import utility as u 
import game as g 
import heapq
from collections import defaultdict

#Transposition Table and iteritive deepening 
#Game table for each peice thats adds or subtracts value based on piece position 

def alpha_prune_ID(board, turn, color, depth, alpha, beta):    
        if depth == 0 or is_leaf_node():
            return g.evaluate(board)
        if turn == True:
            max_eval = float("-inf")
            for move in best_moves(board, color):   
                
                new_board = u.apply_move(board, move[2], move[3])
                eval = alpha_prune(new_board, False, color, depth - 1, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        if turn == False:
            min_eval = float("inf")
            for move in u.possible_moves(board, u.opponent_color(color)): #terrible system for color lol
                new_board = u.apply_move(board, move[2], move[3])
                eval = alpha_prune(new_board, True, u.opponent_color(color), depth - 1, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                        break
            return min_eval
            
def best_moves(board):
     ...
     




def is_leaf_node(board,depth):
     ...
     #checkmate, stalemate, not enought material to win or depth = 0

def iterative_deapening(board, turn, color, depth, alpha, beta):
    found_moves = defaultdict(list)
    max_eval = float("-inf")
    depth_bound = 1
    for depth_bound in range(1,depth+1):
        eval = alpha_prune(board, turn, color, depth_bound, alpha, beta)
        found_moves.append[eval ,board ,depth_bound, turn, color ]

        max_eval = max(max_eval,eval)
    return max_eval 

    
        

