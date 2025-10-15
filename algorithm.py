import board as b 
import pieces as p 
import utility as u 
import game as g 
import heapq
import random


#Transposition Table and iteritive deepening 
#Game table for each peice thats adds or subtracts value based on piece position 

TT = {}



num_squares = 64
piece_types = 12 #types of pieces x 2 colors 
ZOBRIST_TABLE = [
    [random.getrandbits(64) for _ in range(piece_types + 1)]
    for _ in range(num_squares)
]
ZOBRIST_SIDE = random.getrandbits(64)

def find_key(board,turn): #returns unique id
    piece_index = {
    ("white", "Pawn"): 0,  ("white", "Knight"): 1, ("white", "Bishop"): 2,
    ("white", "Rook"): 3,  ("white", "Queen"): 4,  ("white", "King"): 5,
    ("black", "Pawn"): 6,  ("black", "Knight"): 7, ("black", "Bishop"): 8,
    ("black", "Rook"): 9,  ("black", "Queen"): 10, ("black", "King"): 11,
    }

    z_table = 0
    for r in range(8):
        for c in range(8):
            square = board[r][c]
            if u.empty(square):
                continue
            piece_id = piece_index[square.color, square.name]
            square_id = r * 8 + c
            z_table ^= ZOBRIST_TABLE[square_id][piece_id]
    if turn == False:
        z_table ^= ZOBRIST_SIDE
        #castle and en passant
    return z_table
    
def iterative_deepening(board, turn, color, depth, alpha, beta):
    depth_bound = 1
    for depth_bound in range(1,depth):
        eval = alpha_prune(board, turn, color, depth_bound, alpha, beta)
        key = find_key(board, turn)
        TT[key] = [{"eval": eval, "depth": depth, "turn": turn, "color": color, "best_move": move}]

       
    return best_moves 

def alpha_prune(board, turn, color, depth, alpha, beta):    
        move = None
        key = find_key(board, turn)
        if depth == 0 or end_of_game :
            return g.evaluate(board)
        if turn == True:
            max_eval = float("-inf")
            for move in u.possible_moves(board,color):
                if key in TT and depth >= TT[key]["depth"] :
                     best_move == TT[key]["best_move"]
                     new_board = u.apply_move(best_move)
                else: new_board = u.apply_move(board, move[2], move[3])
                eval = alpha_prune(new_board, False, color, depth - 1, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                TT[key] =  {"eval": eval, "depth": depth, "turn": True, "color": color, "best_move": move}
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
                TT[key] =  {"eval": eval, "depth": depth, "turn": False, "color": u.opponent_color(color),"best_move": move}
                if beta <= alpha:
                        break
            return min_eval
            

     




def end_of_game(board,depth):
     ...
     #checkmate, stalemate, not enought material to win or depth = 0


        

