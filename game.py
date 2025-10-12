import board as b 
import pieces as p 
import utility as u 


class Player:
    def __init__(self, color: str, pieces_taken = []):
        self.color = color    
        self.pieces_taken = []
        self.turn = None  #set at start of game and changed after each move
    
    def move_piece(self, board, start_pos, end_pos):
        c, r = start_pos
        end_c, end_r = end_pos
        if not u.empty(board, end_c, end_r): self.capture(board, end_pos)
        board[end_c][end_r] = board[c][r]
        board[c][r].position = (end_c, end_r)
        board[c][r] = " "
        if u.is_legal(board.move):
            return board

    def capture(self, board, position):
        c, r = position
        board[c][r].position = None
        self.pieces_taken.append(board[c][r])

    def evaluate(board):
        ...
             

    
   
    
  
    #dont need aplly actions cant do more than one move in a row, black has to respond 
    #maybe just make 2 players using Player class

    #need a oposing move function that can predict responses in order to look further down the tree 
    #instead I could use another engine to do the response moves which I then send back to the tree to keep exploring
