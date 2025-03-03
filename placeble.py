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
        # TODO: validate selected pos is currently empty
        return True
