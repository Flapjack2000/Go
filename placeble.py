'''
Author: Zach Williams and Evan Dahl
date: 3/23/2025
Title: Placeable Abstract Class
Purpose: this file assigns a player color and starts checking for valid placement
'''
from abc import ABC, abstractmethod
from player_colors import PlayerColors
from position import Position

class Placeble(ABC):
    '''
    To be inherited by GamePiece and represents a placeable piece with its color

    Attributes:
        color (PlayerColors): an instance of player color that represents the players color either black or white
    Methods:
        color(): return the private variable color
        is_valid_placement(): returns Ture or False for basic placement conditions
    '''
    def __init__(self, color: PlayerColors):
        # uses setter to check errors
        if not isinstance(color, PlayerColors):
            raise TypeError('Color must be of type PlayerColors.')

        # Color must be black or white
        if color not in (PlayerColors.WHITE, PlayerColors.BLACK):
            raise ValueError("Color must be white or black.")
        self.__color: PlayerColors = color

    @property
    def color(self) -> PlayerColors:
        '''
        Returns the private variable color

        Returns:
            PlayerColors: instance of player color that represents the players color either black or white
        '''
        return self.__color

    @abstractmethod
    def __str__(self) -> str:
        '''
        Starts the string method to be inherited by GamePiece

        Returns:
             str: The name of the GamePiece
        '''
        pass

    @abstractmethod
    def is_valid_placement(self, pos: Position, board) -> bool:
        '''
        Returns Ture or False for basic placement conditions

        Args:
            pos(Position): the coordinates of the desired placement
            board(list[list]): The current board state

        '''
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
