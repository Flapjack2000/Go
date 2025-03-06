from placeble import Placeble
from player_colors import PlayerColors
from position import Position

class GamePiece(Placeble):
    def __init__(self, color: PlayerColors):
        super().__init__(color)
        self.color = color

    def is_valid_placement(self, pos: Position, board: list[[]]):
        if super().is_valid_placement(pos, board):
            neighbor_positions = [Position(pos.row - 1, pos.col), Position(pos.row, pos.col - 1), Position(pos.row + 1, pos.col), Position(pos.row, pos.col + 1)]
            for nb_pos in neighbor_positions:
                # The piece or None at the neighboring position
                nb_piece = board[nb_pos.row][nb_pos.col]

                # check if the neighboring position is empty
                if super().is_valid_placement(nb_pos, board):
                    return True

                # check if the neighboring position is a wall
                elif not super().is_valid_placement(nb_pos, board) and not isinstance(nb_piece, PlayerColors):
                    pass

                # check if the stone at the neighboring position is the current player's color
                elif nb_piece.color == self.color:
                    return True
            return False
        return False

    def __eq__(self, other):
        return self.color == other.color

    def __str__(self):
        return f"{self.color} Piece"
