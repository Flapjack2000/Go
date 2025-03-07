from player_colors import PlayerColors

class GamePlayer:
    def __init__(self, player_color: PlayerColors, capture_count: int = 0, skip_count: int = 0):
        self.player_color: PlayerColors = player_color
        self.capture_count: int = capture_count
        self.skip_count: int = skip_count

    @property
    def player_color(self) -> PlayerColors:
        return self.__player_color

    @player_color.setter
    def player_color(self, player_color: PlayerColors):
        # Check color type
        if not isinstance(player_color, PlayerColors):
            raise TypeError('Color must be of type PlayerColors.')
        self.__player_color: PlayerColors = player_color

        # Player's color must be black or white
        if player_color not in (PlayerColors.WHITE, PlayerColors.BLACK):
            raise ValueError("Color must be white or black.")

    @property
    def capture_count(self) -> int:
        return self.__capture_count

    @capture_count.setter
    def capture_count(self, capture_count: int):
        if not isinstance(capture_count, int):
            raise TypeError('Capture count must be of type int.')
        if capture_count < 0:
            raise ValueError("Capture count must be at least 0.")
        self.__capture_count: int = capture_count

    @property
    def skip_count(self):
        return self.__skip_count

    @skip_count.setter
    def skip_count(self, skip_count: int):
        if not isinstance(skip_count, int):
            raise TypeError('Skip count must be of type int.')
        if skip_count < 0:
            raise ValueError('Skip count must be at least 0.')
        self.__skip_count: int = skip_count

    def __str__(self) -> str:
        return f"Player {self.player_color}"
