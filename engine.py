import pieces as p 
import utility as u
import board as b
import game as g
import algorithm as a


#evaluate the game state in order to find lowest path_cost
#start simple because could get very coplicated 
def evaluate(board,color):
    evaluation = 0
    return evaluation


#King Saftey 
#Pawn Structure 
#Piece development 
#Trade offs (ex: knight and bishops > rook and awn )

#can make value any value as long as the proportions stay the same 
#can evaluate pieces seperatly 
#try different strategies for find weights  (saw comment about genetic algorithm)



def total_pieces(board,color: str):
    piece_count = 0
    for x in range(8):
        for y in range(8):
            if not u.empty(board,x,y):
                if board[x][y].color == color:
                    piece_count+=1 
    return piece_count

def total_piece_value(board, color):
    total_value = 0
    for x in range(8):
        for y in range(8): 
            if not u.empty(board,x,y):
                if board[x][y].color == color: 
                    total_value+=board[x][y].value
                    print(board[x][y].name)
    return total_value

def opponent_piece_value(board,color):
    total_value = 0
    for x in range(8): 
        for y in range(8):
            if not u.empty(board, x,y):
                if board[x][y].color != color:
                    total_value+=board[x][y].value
    return total_value

def value_difference(board, color):
    total_piece_value(board,color) - opponent_piece_value(board,color)

def is_protected(board,color,position):
    for move in u.possible_moves(board,color):
        if move[3] == position:
            return True 
    return False 
    
def is_under_attack(board,color,position):
    for move in u.possible_moves(board, u.opponent_color(color)): #Opponents moves 
        if move[3] == position:
            return True 
    return False 
    

    








            

