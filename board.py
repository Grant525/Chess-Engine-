import json 
import pieces as p
import utility as u

class Board: 
    def __init__(self):
        self.board = Board
    
   
    def create_board():
            board = [[" " for _ in range(8)] for _ in range(8)] 
            return board
        
     
    def reset_board(board):
        for a in range(8): 
            board[1][a] = p.Pawn(color = "white", position = (1, a), id = a + 1)
            board[6][a] = p.Pawn(color = "black", position = (6, a), id = a + 9) 
            if a == 0 or a == 7:
                board[0][a] = p.Rook(color = "white", position = (0, a), id = 1 if a == 0 else 2)
                board[7][a] = p.Rook(color = "black", position = (7, a), id = 3 if a == 0 else 4)
            if a == 1 or a == 6:
                board[0][a] = p.Knight(color = "white", position = (0, a), id = 1 if a == 1 else 2)
                board[7][a] = p.Knight(color = "black", position = (7, a), id = 3 if a == 1 else 4)
            if a == 2 or a == 5:
                board[0][a] = p.Bishop(color = "white", position = (0, a), id = 1 if a == 2 else 2)
                board[7][a] = p.Bishop(color = "black", position = (7, a), id = 3 if a == 2 else 4)
        board[0][3] = p.Queen(color = "white", position = (0, 3), id = 1)
        board[7][3] = p.Queen(color = "black", position = (7, 3), id = 2)
        board[0][4] = p.King(color = "white", position = (0, 4), id = 1) 
        board[7][4] = p.King(color = "black", position = (7, 4), id = 2)
        

  
    


      
                   

                