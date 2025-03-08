
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

        # Board dimension validation
        if not isinstance(nrows, int):
            raise TypeError('Number of rows must be a positive integer.')
        if not isinstance(ncols, int):
            raise TypeError('Number of columns must be a positive integer.')

        if nrows not in self.valid_board_lengths:
            raise ValueError(f"Number of rows must be one of {self.valid_board_lengths}.")
        if ncols not in self.valid_board_lengths:
            raise ValueError(f"Number of columns must be one of {self.valid_board_lengths}.")

        # TODO: Write initial message
        self.message = "First message"

    @property
    def current_player(self) -> GamePlayer:
        return self.__current_player

    @current_player.setter
    def current_player(self, player: GamePlayer):
        # REVIEW: validation
        if not isinstance(player, GamePlayer):
            raise TypeError('Players must be of type GamePlayer.')
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

    # CAPTURE SURROUNDED PIECES ON PLACEMENT 
    # 1) Place piece
    # 2) Find neighboring opponent pieces 
    # 3) For each opponent piece found, find their ally neighbors. 
        # a) Put each neighboring opponent piece in a set (of their own). 
        # b) For each opponent piece in each set, add its neighboring allies to the set.
        # c) Because it's a set and won't increase its cardinality forever 
            # into infinity when it's added to, it should stop iterating when all members are found. 
        # d) Alternatively, this might be a cool use case for recursion.
        # Now we have our neighboring clusters (sets) of enemies 
    
    # 4) Check if the clusters are surrounded 
        # a) Clusters are surrounded if all of their members neighbor only:
            # i) Their cluster-mates
            # ii) Enemy pieces 
            # iii) Board edges
        # b) Perhaps that can be restated:
            # If none of the pieces in the cluster touch an empty place, 
            # then the cluster is surrounded.
    
    # SAVE BOARD
    # Keep list of board copies (not deep copies)
    # Might need to track other data like scores
    # Use index variable for current board
    # Make move: 
    #     - don't repeat boards (if board in past_boards)
    #     - index++
    # Undo: 
    #     - board = past_boards[index - 1]
    #     - index--


