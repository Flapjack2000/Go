
from game_piece import GamePiece
from game_player import GamePlayer
from player_colors import PlayerColors

class GoModel:
    def __init__(self, nrows: int = 6, ncols: int = 6):
        # The first player is BLACK
        self.current_player = GamePlayer(PlayerColors.BLACK)

        # Board dimensions
        self.nrows = nrows
        self.ncols = ncols

        # Generate an empty board based on dimensions
        self.board = [[None] * self.ncols] * self.nrows

        # TODO: Write initial message
        self.message = ""

    @property
    def current_player(self) -> GamePlayer:
        return self.__current_player

    @current_player.setter
    def current_player(self, player: GamePlayer):
        # TODO: validation
        self.__current_player = player

    @property
    def nrows(self) -> int:
        return self.__nrows

    @nrows.setter
    def nrows(self, nrows: int):
        # TODO: validation
        self.__nrows = nrows

    @property
    def ncols(self) -> int:
        return self.__ncols

    @ncols.setter
    def ncols(self, ncols: int):
        # TODO: validation
        self.__ncols = ncols

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, board: list[list[GamePiece | None]]):
        # TODO: validation
        self.__board = board

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        # TODO: validation
        self.__message = message

