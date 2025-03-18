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
		self.player_b = GamePlayer(PlayerColors.WHITE)
		self.player_w = GamePlayer(PlayerColors.BLACK)

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

		self.__nrows = nrows
		self.__ncols = ncols

		# Generate an empty board based on dimensions
		self.__board: list[list[None]] = [[None] * self.ncols] * self.nrows

		# List of previous board states
		self.__past_boards: list = []

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
		self.board_history.append(copy(board))

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

		if not isinstance(piece, (GamePiece, None)):
			raise TypeError('Piece must be of type GamePiece or None.')
		self.__board[pos.row][pos.col] = piece

		# Setting a piece clears any streak of passes
		self.consecutive_passes = 0

	def set_next_player(self):
		# Toggle between the two players
		self.__current_player = (self.player_b) if (self.__current_player == self.player_w) else (self.player_w)

	def pass_turn(self) -> None:
		self.consecutive_passes += 1
		# REVIEW: should we set_next_player, or will that happen in go_gui_view???
		#	find out before writing code lol

	def is_game_over(self):
		# If both players passed, the game is over
		if self.consecutive_passes >= 2:
			return True

		# Check if there are any more places to play
		for r_index, row in enumerate(self.__board):
			for c_index, ele in row:
				if self.is_valid_placement(Position(r_index, c_index), ele):
					return False
		return True

	def is_valid_placement(self, pos: Position, piece: GamePiece) -> bool:
		if not piece.is_valid_placement(pos, self.board):
			return False
			
		potential_board = copy(self.board)
		potential_board[pos.row][pos.col] = piece

		if self.check_ko(potential_board):
			return False

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

	def clear_all_flags(self, board):
		for row_i, row in enumerate(board):
			for col_i, ele in enumerate(row):
				if isinstance(ele, GamePiece):
					ele.flag = False

	def find_group(self, board, target_color: PlayerColors, target_coords: tuple[int]) -> set:
		pass

	def capture(self):
		# look for groups of stones connected vertically and horizontally - NOT DIAGONALLY
		# if any of them are completely surrounded with no liberties, then they are captureable
		
		prev_piece = None
		prev_pos = None
		# Find previously played piece because any captures will happen next to that piece
		for row_i, row in enumerate(self.board_history[-1]):
			for col_i, ele in enumerate(row):
				if self.board[row_i][col_i] != ele:
					prev_piece: GamePiece = self.board[row_i][col_i]
					prev_piece: tuple[int] = (row_i, col_i)

		# If no change was found, then it was a pass and nothing happens
		if prev_piece is None or prev_pos is None:
			# TODO: remove print when done testing
			print("No change found")
			return

		# We want to capture the pieces of the opponent of whoever played the last stone
		target_color: PlayerColors = prev_piece.color.opponent()


		left_coord = (prev_pos[0], prev_pos[1] - 1)
		right_coord = (prev_pos[0], prev_pos[1] + 1)
		up_coord = (prev_pos[0] - 1, prev_pos[1])
		down_coord = (prev_pos[0] + 1, prev_pos[1])

		groups: set[set] = set()

		groups.add(self.find_group(
			board = self.board, 
			target_color = target_color,
			target_coords = left_coord))

		groups.add(self.find_group(
			board = self.board, 
			target_color = target_color,
			target_coords = right_coord))

		groups.add(self.find_group(
			board = self.board, 
			target_color = target_color,
			target_coords = up_coord))

		groups.add(self.find_group(
			board = self.board, 
			target_color = target_color,
			target_coords = down_coord))
		
		# Remove appropriate stones

		# Clear all flags just in case
		self.clear_all_flags(self.board)

		# Record the board state for undo/ko 
		self.record_board_state(self.board)
