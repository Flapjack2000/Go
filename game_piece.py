from placeble import Placeble
from player_colors import PlayerColors
from position import Position

class GamePiece(Placeble):
    def __init__(self, color: PlayerColors):
        super().__init__(color)

    def is_valid_placement(self, pos: Position, board):
        # Basic validation
        if not super().is_valid_placement(pos, board):
            return False

        is_possible = False

        neighbor_positions = [Position(pos.row - 1, pos.col), Position(pos.row, pos.col - 1), Position(pos.row + 1, pos.col), Position(pos.row, pos.col + 1)]
        for nb_pos in neighbor_positions:

            # Check if the neighboring position is off the board, which means the piece is being placed on the edge
            if not 0 <= nb_pos.row < len(board):
                continue
            if not 0 <= nb_pos.col < len(board[0]):
                continue

            # Check if there is an empty space nearby
            if board[nb_pos.row][nb_pos.col] is None:
                is_possible = True

            # Check if there is a piece of the same color nearby
            elif board[nb_pos.row][nb_pos.col].color == self.color:
                is_possible = True

        return is_possible

    def __eq__(self, other):
        return self.color == other.color

    def __str__(self):
        return f"{self.color} Piece"

    def __repr__(self):
        return f'{self.color}'
