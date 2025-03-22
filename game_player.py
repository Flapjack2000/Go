"""
Author: Zach Williams and Evan Dahl
date: 3/23/2025
Title: Game_Player class
Purpose: Initializes the Game Player to store player specific game information
"""
from player_colors import PlayerColors

class GamePlayer:
    """
    Represents a game player as an instance of PlayerColors and tracks capture and skip counts

    Attributes:
        player_colors (PlayerColors): the current player color as an instance of PlayerColors
        capture_count (int): the number of captured pieces by the player
        skip_count (int): the number of skipped turns by the player
    Methods:
        player_color(): A property that returns the current player color as an instance of PlayerColors
        capture_count(): A property and property setter that can set and/or return the number of captured pieces
        skip_count(): A property and property setter that can set and return the number of skipped turns
        __str__(): Returns the string representation of the game player
    """
    def __init__(self, player_color: PlayerColors, capture_count: int = 0, skip_count: int = 0):
        """
        Initializes the game player with an instance of PlayerColors, a number for capture count, and a number for skip count

        Args:
            player_color (PlayerColors): the current player color as an instance of PlayerColors
            capture_count (int): the number of captured pieces by the player
            skip_count (int): the number of skipped turns by the player
        Raises:
            TypeError: if player_colors is not an instance of PlayerColors

        """
        # Check color type
        if not isinstance(player_color, PlayerColors):
            raise TypeError('Player color must be of type PlayerColors.')

        # Player's color must be black or white
        if player_color not in (PlayerColors.WHITE, PlayerColors.BLACK):
            raise ValueError("Player color must be white or black.")

        self.__player_color: PlayerColors = player_color
        self.capture_count: int = capture_count
        self.skip_count: int = skip_count

    @property
    def player_color(self) -> PlayerColors:
        """
        A property that returns the current player color as an instance of PlayerColors
        """
        return self.__player_color

    @property
    def capture_count(self) -> int:
        """
        A property that returns the number of captured pieces
        """
        return self.__capture_count

    @capture_count.setter
    def capture_count(self, capture_count: int):
        """
        A property setter that sets the number of captured pieces by the player

        Args:
            capture_count (int): the number of captured pieces by the player
        Raises:
            TypeError: if capture_count is not an int
            ValueError: if capture_count is less than 0
        """
        if not isinstance(capture_count, int):
            raise TypeError('Capture count must be of type int.')
        if capture_count < 0:
            raise ValueError("Capture count must be at least 0.")
        self.__capture_count: int = capture_count

    @property
    def skip_count(self):
        """
        A property that returns the number of skipped turns by the player
        """
        return self.__skip_count

    @skip_count.setter
    def skip_count(self, skip_count: int):
        """
        A property setter that sets the number of skipped turns by the player

        Args:
            skip_count (int): the number of skipped turns by the player
        Raises:
            TypeError: if skip_count is not an int
            ValueError: if skip_count is less than 0
        """
        if not isinstance(skip_count, int):
            raise TypeError('Skip count must be of type int.')
        if skip_count < 0:
            raise ValueError('Skip count must be at least 0.')
        self.__skip_count: int = skip_count

    def __str__(self) -> str:
        """
        Returns the string representation of the game player
        """
        return f"Player {self.player_color}"
