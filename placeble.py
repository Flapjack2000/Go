from abc import ABC, abstractmethod
from player_colors import PlayerColors
from position import Position

class Placeble(ABC):
    def __init__(self, color: PlayerColors):
        # uses setter to check errors
        self.color: PlayerColors = color

    # FAIL: test_color_property
    @property
    def color(self) -> PlayerColors:
        return self.__color

    @color.setter
    def color(self, color: PlayerColors):
        # Check color type
        if not isinstance(color, PlayerColors):
            raise TypeError('Color must be of type PlayerColors.')
        self.__color: PlayerColors = color

        # Color must be black or white
        if color not in (PlayerColors.WHITE, PlayerColors.BLACK):
            raise ValueError("Color must be white or black.")

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def is_valid_placement(self, pos: Position, board) -> bool:
        # Check pos is a Position instance
        if not isinstance(pos, Position):
            return False

        # Check pos is on the board
        if (not 0 <= pos.row < len(board)) or (not 0 <= pos.col < len(board[0])):
            return False

        # Check that the position is unoccupied
        if board[pos.row][pos.col] is not None:
            return False

        return True
