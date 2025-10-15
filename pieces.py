import utility as u

class Pawn:
    def __init__(self, color: str, position: tuple[int, int], id = None):
        self.name = "Pawn"
        self.color = color    
        self.value = 1
        self.position = position
        self.id = id
               

    def get_moves (self, board):
        c,r = self.position
        possible_moves = []
        id = u.get_id(c, r)
        color = self.color                     
        if u.different_color(board, c+1,r+1,color):
            possible_moves.append("Pawn",id,(c,r),(c+1,r+1 if color == "white" else r-1)) 
        if u.different_color(board, c-1,r+1,color):
            possible_moves.append("Pawn",id,(c,r),(c-1,r+1 if color == "white" else r-1)) 
        if u.empty(board,c,r+1):
            possible_moves.append("Pawn",id,(c,r),(c,r+1 if color == "white" else r-1))
        if u.empty(board,c,r+2) and r == 2:
            possible_moves.append("Pawn",id,(c,r),(c,r+2 if color == "white" else r-2))
        #en passant and promotion 
        return possible_moves


class Rook:
    def __init__(self, color: str, position: tuple[int, int],id = None):
        self.name = "Rook"
        self.color = color
        self.value = 5
        self.position = position
        self.id = id

    def move(self, new_position: tuple[int, int]):
        
        self.position = new_position


    def get_moves(self, board):
        possible_moves = []
        id = u.get_id(c, r)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]  # right, left, down, up
        c,r = self.position
        color = self.color
        for x, y in directions:
            new_c, new_r = c + x, r + y
            if u.in_bounds(new_c, new_r):
                if u.empty(board, new_c, new_r):
                    possible_moves.append(("Rook", id, (c, r), (new_c, new_r)))
                elif u.different_color(board, new_c, new_r, color):
                    possible_moves.append(("Rook", id, (c, r), (new_c, new_r)))
        return possible_moves
        
class Knight:
    def __init__(self, color: str, position: tuple[int, int],id = None):
        self.name = "Knight"
        self.color = color
        self.value = 3
        self.position = position
        self.id = id

    def move(self, new_position: tuple[int, int]):
        # Implement knight-specific movement rules
        self.position = new_position
    
    def get_moves(self, board):
        possible_moves = []
        id = u.get_id(c, r)
        directions = [(2,1), (2,-1), (-2,1), (-2,-1),(1,2), (1,-2), (-1,2), (-1,-2)] 
        c,r = self.position
        color = self.color
        for x, y in directions:
            new_c, new_r = c + x, r + y
            if u.in_bounds(new_c, new_r):
                if u.empty(board, new_c, new_r):
                    possible_moves.append(("Knight",id,(c, r), (new_c, new_r)))
                elif u.different_color(board, new_c, new_r, color):
                    possible_moves.append(("Knight",id, (c, r), (new_c, new_r)))
            else: return None
        return possible_moves 


class Bishop:
    def __init__(self, color: str, position: tuple[int, int],id = None):
        self.name = "Bishop"
        self.color = color
        self.value = 3
        self.position = position
        self.id = id

    def move(self, new_position: tuple[int, int]):
        # Implement bishop-specific movement rules
        self.position = new_position

    def get_moves(self, board):
        possible_moves = []
        id = u.get_id(c, r)
        directions = [(1,1), (1,-1), (-1,1), (-1,-1)] 
        c,r = self.position
        color = self.color
        for x, y in directions:
            new_c, new_r = c + x, r + y
            if u.in_bounds(new_c, new_r):
                if u.empty(board, new_c, new_r):
                    possible_moves.append(("Bishop",id,(c, r), (new_c, new_r)))
                elif u.different_color(board, new_c, new_r, color):
                    possible_moves.append(("Bishop",id, (c, r), (new_c, new_r)))
            else: return None
        
        return possible_moves 

class Queen:
    def __init__(self, color: str, position: tuple[int, int],id = None):
        self.name = "Queen"
        self.color = color
        self.value = 9
        self.position = position
        self.id = id

    def move(self, new_position: tuple[int, int]):
        # Implement queen-specific movement rules
        self.position = new_position
    
    def get_moves(self,board):
        possible_moves = []
        id = u.get_id(c, r)
        directions = [(1,1), (1,-1), (-1,1), (-1,-1), (1,0), (-1,0), (0,1), (0,-1)] 
        c,r = self.position
        color = self.color
        for x, y in directions:
            new_c, new_r = c + x, r + y
            while u.in_bounds(new_c, new_r):
                if u.empty(board, new_c, new_r):
                    possible_moves.append(("Queen", id,(c, r),(new_c, new_r)))
                elif u.different_color(board, new_c, new_r, color):
                    possible_moves.append(("Queen", id,(c, r),(new_c, new_r)))
                    break
                else: 
                    break
        return possible_moves 

class King:
    def __init__(self, color: str, position: tuple[int, int], id = None):
        self.name = "King"
        self.color = color
        self.value = 0 #variable, has worth in end game 
        self.position = position
        self.id = id

    def move(self, new_position: tuple[int, int]):
        # Implement king-specific movement rules
        self.position = new_position
    
    def get_moves(self, board):
        possible_moves = []
        id = u.get_id(c, r)
        directions = [(1,1), (1,-1), (-1,1), (-1,-1), (1,0), (-1,0), (0,1), (0,-1)]
        c,r = self.position 
        color = self.color
        for x, y in directions:
            new_c, new_r = c + x, r + y
            if u.in_bounds(new_c, new_r):
                if u.empty(board, new_c, new_r):
                    possible_moves.append(("King", id,(c, r),(new_c, new_r)))
                    break
                elif u.different_color(board, new_c, new_r, color):
                    possible_moves.append(("King", id,(c, r),(new_c, new_r)))
                else: return None
        return possible_moves
    
    
    
    
    #def capture(self, pieces, position):
  




    

     
    
    