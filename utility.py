
def in_bounds(c,r):
        return 0 <= r < 8 and 0 <= c < 8 
        
def empty(board,c,r):
        return board[c][r] == " "
        
def same_color (board,c,r,color):
        return board[c][r].color == color
        
def different_color(board,c,r,color):
        return board[c][r].color != color

def get_id(board,c,r):
        return board[c][r].id

def apply_move(board, start_pos, end_pos):
        new_board = [row[:] for row in board]
        c, r = start_pos
        end_c, end_r = end_pos
        new_board[end_c][end_r] = board[c][r]
        new_board[c][r].position = (end_c, end_r)
        new_board[c][r] = " "
        return new_board

def checkmate(self, board, color): 
        if possible_moves(board, color) == [] and in_check():
            return True
        return False

def in_check(self, board, color): 
        for moves in possible_moves(board):
            if moves[3] == king_pos(board) and moves.color != color:
                return True 
        return False

def stalemate(board, color):
        if possible_moves(board, color) == [] and not in_check():
            return True
        
def king_pos(board, color):
        for x,y in board:
            if board[x][y].name == "King" and board[x][y].color == color:
                return (x,y)
            
def possible_moves(board, color): 
        possible_moves = []
        for c in range(8):
            for r in range(8):
                if board[c][r].color == color and not empty(board,c,r):
                    possible_moves.extend(board[c][r].get_moves(board))
        for moves in possible_moves:
            if in_check(apply_move(board, possible_moves, color)):
                possible_moves.remove(moves)
        return possible_moves


def is_legal(board, move):
        if in_check(apply_move(board, move), board, color):
              return False 
        return True



def opponent_color(color):
    if color == "white":
        return "black" 
    if color == "black":
        return "white"

