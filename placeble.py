from abc import ABC, abstractmethod
from player_colors import PlayerColors
from position import Position
from typing import List, Optional

# FIXME: Causes circular import since GamePiece relies on Placeble
from game_piece import GamePiece

class Placeble(ABC):
    def __init__(self, color: PlayerColors):
        # uses setter to check errors
        self.color: PlayerColors = color

    @property
    def color(self) -> PlayerColors:
        return self.__color

    @color.setter
    def color(self, color: PlayerColors):
        # TODO: raise ValueError for bad color???
        #one of these should work for checking color pretty sure its the second one but it would be nice if it was the first
        if PlayerColors.WHITE or PlayerColors.BLACK:
            raise ValueError

        if (not isinstance(color, PlayerColors.WHITE)) or (not isinstance(color, PlayerColors.BLACK)):
            raise ValueError

        if not isinstance(color, PlayerColors):
            raise TypeError('Color must be of type PlayerColors.')
        self.__color: PlayerColors = color

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def is_valid_placement(self, pos: Position, board: List[List[Optional[GamePiece]]]) -> bool:
        if not isinstance(pos, Position):
            return False
        # TODO: validate selected pos is on the board
        #potential solution not sure
        if pos not in board:
            return False
        # TODO: validate selected pos is currently empty
        #this should work
        if board[pos[0]][pos[1]] is not None:
            return False

        return True
