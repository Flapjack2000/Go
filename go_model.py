from game_piece import GamePiece
from game_player import GamePlayer
from player_colors import PlayerColors
from position import Position
from copy import copy, deepcopy

class UndoException(Exception):
    """
    Raised when undo is not possible.
    """
    pass

def are_boards_identical(board1, board2) -> bool:
    for row_i, row in enumerate(board1):
        for col_i, ele in enumerate(row):
            other = board2[row_i][col_i]
            if type(ele) != type(other):
                return False
            if isinstance(ele, GamePiece) and isinstance(other, GamePiece):
                if ele != other:
                    return False
    return True

class GoModel:
    def __init__(self, nrows: int = 6, ncols: int = 6):

        # Instantiate players - need consistent instances to keep track of capture count and skip count
        self.player_b = GamePlayer(PlayerColors.BLACK)
        self.player_w = GamePlayer(PlayerColors.WHITE)

        # The first player is BLACK
        self.__current_player = self.player_b

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

        # Make sure the board is a square
        if nrows != ncols:
            raise ValueError("Number of rows must equal number of columns so that the board is square.")

        self.__nrows = nrows
        self.__ncols = ncols

        # Generate an empty board based on dimensions
        self.__board = []
        for _ in range(nrows):
            self.__board.append([None for _ in range(ncols)])

        # List of previous board states
        self.__past_boards: list = []

        self.prev_placement = None

        # Tracks the number of consecutive passes, game ends after both players pass
        self.consecutive_passes = 0

        # REVIEW: Edit initial message?
        self.message = "Welcome to Go. Black goes first."

    @property
    def current_player(self) -> GamePlayer:
        return self.__current_player

    @property
    def board_history(self):
        return self.__past_boards

    def record_board_state(self, board):
        self.board_history.append(deepcopy(board))

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
        if not (0 <= pos.row < self.nrows) or not (0 <= pos.col < self.ncols):
            raise ValueError('Position out of bounds.')
        return self.board[pos.row][pos.col]

    def set_piece(self, pos: Position, piece: GamePiece = None):
        if not isinstance(pos, Position):
            raise TypeError('Position must be of type Position.')

        if not (0 <= pos.row < len(self.board)) or not (0 <= pos.col < len(self.board[0])):
            raise ValueError('Position out of bounds.')

        if not isinstance(piece, (GamePiece, type(None))):
            raise TypeError('Piece must be of type GamePiece or None.')

        self.__board[pos.row][pos.col] = piece

        # Setting a piece clears any streak of passes
        self.consecutive_passes = 0

        # Record the position for capturing
        self.prev_placement = (piece, (pos.row, pos.col))

        # Record the board state for undo/ko
        self.record_board_state(self.board)

    def set_next_player(self):
        # Toggle between the two players
        if self.current_player == self.player_w:
            self.__current_player = self.player_b
        elif self.current_player == self.player_b:
            self.__current_player = self.player_w
        self.message = f"Now it's {self.current_player.player_color.name}'s turn."

    def pass_turn(self) -> None:
        self.consecutive_passes += 1
        self.prev_placement = None
        self.set_next_player()

    def is_game_over(self):
        # If both players passed, the game is over
        if self.consecutive_passes >= 2:
            return True

        # Check if there are any more places to play
        for r_index, row in enumerate(self.board):
            for c_index, ele in enumerate(row):
                if ele is None:
                    return False
        return True

    def is_valid_placement(self, pos: Position, piece: GamePiece) -> bool:
        if not piece.is_valid_placement(pos, self.board):
            return False

        potential_board = copy(self.board)
        potential_board[pos.row][pos.col] = piece

        if self.check_ko(potential_board):
            return False

        # You can also place a piece if it captures an enemy group
        # The enemy group must be in atari (only one liberty)






    def check_ko(self, potential_board) -> bool:
        # Ko isn't actually possible until 2 moves have been made
        if len(self.board_history) > 2:
            # REVIEW: is -2 the right index???
            if are_boards_identical(potential_board, self.board_history[-2]):
                return True
        return False

    def calculate_score(self) -> list:
        pass

    def undo(self):
        # Check that undoing is possible
        if len(self.board_history) == 0:
            raise UndoException("No moves left to undo.")

        # Go back one move and remove it from the history
        self.__board = self.board_history.pop()

    def lower_all_flags(self):
        for row_i, row in enumerate(self.board):
            for col_i, ele in enumerate(row):
                if isinstance(ele, GamePiece):
                    ele.lower_flag()

    def capture(self):
        # look for groups of stones connected vertically and horizontally - NOT DIAGONALLY
        # if any of them are completely surrounded with no liberties, then they are captureable

        if self.prev_placement is None:
            return

        prev_piece = self.prev_placement[0]
        prev_coord = self.prev_placement[1]

        # We want to capture the pieces of the opponent of whoever played the last stone
        target_color: PlayerColors = prev_piece.color.opponent()

        left_coord = (prev_coord[0], prev_coord[1] - 1)
        right_coord = (prev_coord[0], prev_coord[1] + 1)
        up_coord = (prev_coord[0] - 1, prev_coord[1])
        down_coord = (prev_coord[0] + 1, prev_coord[1])

        # look for groups of opponents in all 4 cardinal directions
        # group elements are tuples in the format: (piece, (row, col))
        left_group = self.find_group(
            board = self.board,
            target_color = target_color,
            target_coords = left_coord)

        right_group = self.find_group(
            board = self.board,
            target_color = target_color,
            target_coords = right_coord)

        up_group = self.find_group(
            board = self.board,
            target_color = target_color,
            target_coords = up_coord)

        down_group = self.find_group(
            board = self.board,
            target_color = target_color,
            target_coords = down_coord)

        groups = (left_group, right_group, up_group, down_group)

        # Find the neighboring spaces of all the pieces in the group
        for group in groups:
            found_empty = False

            for data_pair in group:
                piece, pos = data_pair
                r, c = pos

                left_nb = (r, c - 1)
                right_nb = (r, c + 1)
                up_nb = (r - 1, c)
                down_nb = (r + 1, c)

                neighbors = (left_nb, right_nb, up_nb, down_nb)

                # Check if any of the neighboring spaces are empty. If none of the pieces are touching an empty space, the group is surrounded.
                for nb_coord in neighbors:
                    try:
                        if self.piece_at(Position(*nb_coord)) is None:
                            found_empty = True
                            break # don't need to keep going

                    # Ignore out of bounds error because board edges count towards being surrounded
                    except ValueError:
                        pass

            # If the group is surrounded raise its pieces' flags
            if not found_empty:
                for data_pair in group:
                    piece, pos = data_pair
                    piece.raise_flag()

            self.remove_flagged_pieces()

            self.prev_placement  = None

    def remove_flagged_pieces(self):
        # Remove all flagged stones from board
        for row_i, row in enumerate(self.board):
            for col_i, ele in enumerate(row):
                if isinstance(ele, GamePiece):
                    self.current_player.capture_count += 1
                    if ele.flag:
                        self.board[row_i][col_i] = None

    def find_group(self, board, target_color: PlayerColors, target_coords: tuple[int, int], group = None) -> list:
        r, c = target_coords

        if group is None:
            group = []

        if (0 <= r < len(board)) and (0 <= c < len(board)):
            piece = board[r][c]

            if piece is None or (piece, (r, c)) in group:
             pass

        # if the piece is the color we are looking for
            elif isinstance(piece, GamePiece):
                if piece.color == target_color:
                    group.append((piece, (r, c)))

                    # look left
                    self.find_group(board, target_color, (r, c - 1), group)

                    # look right
                    self.find_group(board, target_color, (r, c + 1), group)

                    # look up
                    self.find_group(board, target_color, (r - 1, c), group)

                    # look down
                    self.find_group(board, target_color, (r + 1, c), group)
        return group
