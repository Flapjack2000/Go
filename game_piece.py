from placeble import Placeble
from player_colors import PlayerColors
from position import Position

class GamePiece(Placeble):
    def __init__(self, color: PlayerColors):
        super().__init__(color)
        self.color = color

    def is_valid_placement(self, pos: Position, board: list[[]]):
        super().is_valid_placement(pos, board)
        self.pos = pos
        self.board = board

        around_piece = [[(self.pos[0]) - 1, self.pos[1]], [(self.pos[0]) - 1, (self.pos[1]) - 1], [self.pos[0], (self.pos[1]) - 1], [(self.pos[0]) + 1, (self.pos[1]) - 1], [(self.pos[0]) + 1, self.pos[1]], [(self.pos[0]) + 1, (self.pos[1]) + 1], [self.pos[0], (self.pos[1]) + 1], [(self.pos[0]) - 1, (self.pos[1]) + 1]]
        for piece in around_piece:
            if board[piece[0]][piece[1]] == None:
                return True
            if board[piece[0]][piece[1]] != None:
                pass
                #check if is player color or enemy color, if enemy enemy_counter += 1
                #if to run is_valid_placement again if the "piece" being checked is a player piece, maybe add counter for how many player pieces to multiply by
                #number of possible surrounding pieces would be num player pieces times 8, minus 1 for each call of is_valid_placement
                #return false if enemy counter = possible surrounding pieces

    def __eq__(self, other):
        #not sure what to put after self and other
        gamepiece1 = self.color
        gamepiece2 = other.color

        if gamepiece1 == gamepiece2:
            return True
        else:
            return False


    def __str__(self):
        return f"Player {self.color} at {self.pos}"
