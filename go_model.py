from game_piece import GamePiece
from game_player import GamePlayer
from player_colors import PlayerColors
from position import Position

class UndoException(Exception):
    pass

class GoModel:
    def __init__(self, nrows: int = 6, ncols: int = 6):

        self.consecutive_passes = 0

        # The first player is BLACK
        self.__current_player = GamePlayer(PlayerColors.BLACK)

        # Board dimensions
        self.valid_board_lengths = (6, 9, 11, 13, 19)

        # Check for invalid rows and columns
        if not isinstance(nrows, int):
            raise TypeError('Number of rows must be a positive integer.')
        if nrows not in self.valid_board_lengths:
            raise ValueError(f"Number of rows must be one of {self.valid_board_lengths}.")
        if not isinstance(ncols, int):
            raise TypeError('Number of columns must be a positive integer.')
        if ncols not in self.valid_board_lengths:
            raise ValueError(f"Number of columns must be one of {self.valid_board_lengths}.")

        self.__nrows = nrows
        self.__ncols = ncols

        # Generate an empty board based on dimensions
        self.__board: list[list[None]] = [[None] * self.ncols] * self.nrows

        # TODO: Write initial message
        self.message = "First message"

    @property
    def current_player(self) -> GamePlayer:
        return self.__current_player

    @property
    def nrows(self) -> int:
        return self.__nrows

    @property
    def ncols(self) -> int:
        return self.__ncols

    @property
    def board(self):
        return self.__board

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        if not isinstance(message, str):
            raise TypeError('Message must be of type string.')
        self.__message = message

    def piece_at(self, pos: Position) -> GamePiece | None:
        if not isinstance(pos, Position):
            raise TypeError('Position must be of type Position.')
        if not 0 <= pos.row < len(self.board) or 0 <= pos.col < len(self.board[0]):
            raise ValueError('Position out of bounds.')
        return self.board[pos.row][pos.col]

    def set_piece(self, pos: Position, piece: GamePiece = None):
        if not isinstance(pos, Position):
            raise TypeError('Position must be of type Position.')
        if not 0 <= pos.row < len(self.board) or 0 <= pos.col < len(self.board[0]):
            raise ValueError('Position out of bounds.')
        if not isinstance(piece, (GamePiece, None)):
            raise TypeError('Piece must be of type GamePiece or None.')
        self.__board[pos.row][pos.col] = piece

        self.consecutive_passes = 0

    def set_next_player(self):
        self.__current_player = self.__current_player.player_color.opponent()

    def pass_turn(self) -> None:
        self.consecutive_passes += 1

    def is_game_over(self):
        if self.consecutive_passes == 2:
            return True
        for r_index, r in enumerate(self.__board):
            for c_index, c in r:
                if self.is_valid_placement(Position(r_index, c_index), c):
                    return False
        return True

    def is_valid_placement(self, pos: Position, piece: GamePiece) -> bool:
        if piece.is_valid_placement(pos, self.board):
            pass


    def capture(self):
        pass
    def calculate_score(self):
        pass
    def undo(self):
        pass




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
