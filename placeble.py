from abc import ABC, abstractmethod
from player_colors import PlayerColors
from position import Position
from typing import List, Optional

class Placeble(ABC):
    def __init__(self, color: PlayerColors):
        # uses setter to check errors
        self.color: PlayerColors = color

    @property
    def color(self) -> PlayerColors:
        return self.__color

    @color.setter
    def color(self, color: PlayerColors):
        # Color must be black or white
        if color not in (PlayerColors.WHITE, PlayerColors.BLACK):
            raise ValueError

        # Check color type
        if not isinstance(color, PlayerColors):
            raise TypeError('Color must be of type PlayerColors.')
        self.__color: PlayerColors = color

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def is_valid_placement(self, pos: Position, board) -> bool:
        # Check pos is a Position instance
        if not isinstance(pos, Position):
            return False

        # Check pos is on the board
        if pos.col < 0 or pos.row < 0:
            return False
        if pos.col > len(board) - 1 or pos.row > len(board) - 1:
            return False

        # Check that the position is unoccupied
        if board[pos.row][pos.col] is not None:
            return False

        return True
