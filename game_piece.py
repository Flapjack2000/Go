'''
Author: Zach Williams and Evan Dahl
date: 3/23/2025
Title: GamePiece Class inherits Placeble
Purpose: Initializes the Game Piece as an instance of PlayerColors and continues valid placement checks
'''
from placeble import Placeble
from player_colors import PlayerColors
from position import Position

class GamePiece(Placeble):
	'''
	Represents a game piece that is and instance of PlayerColors

	Attributes:
		color (PlayerColors): An instance of PlayerColors either BLACK or WHITE
		flag (bool): True if the game piece has been flagged for capture
	Methods:
		toggle_flag(): sets the flag to the opposite boolean value
		raise_flag(): sets the flag to True
		lower_flag(): sets the flag to False
		is_valid_placement(): returns True if the game piece has a valid placement
		__eq__(): returns the boolean value of the equality of two class objects
		__str__(): returns the string representation of the game piece
	'''
	def __init__(self, color: PlayerColors):
		'''
		Initializes the game piece object and inherits the placeble initializer

		Args:
			color (PlayerColors): An instance of PlayerColors either BLACK or WHITE
			flag (bool): True if the game piece has a flag
		Raises:
			TypeError: if color is not an instance of PlayerColors
			ValueError: if color is not an instance of BLACK or WHITE of PlayerColors

		'''
		super().__init__(color)

		self.flag = False

	def toggle_flag(self):
		'''
		Sets the flag to the opposite boolean value
		'''
		self.flag = not self.flag

	def raise_flag(self):
		'''
		Sets the flag to True
		'''
		self.flag = True

	def lower_flag(self):
		'''
		Sets the flag to False
		'''
		self.flag = False

	def is_valid_placement(self, pos: Position, board):
		'''
		Returns True or False if the position is a valid placement

		Args:
			pos (Position): the position of the placement an instance of Position
			board (list[list]): the current board state
		Returns:
			bool: True if the position is a valid placement and False otherwise
		Raises:
			TypeError: if pos is not an instance of Position
			ValueError: if pos is not in the bounds of the board
		'''
		# Basic validation
		if not super().is_valid_placement(pos, board):
			return False

		is_possible = False

		neighbor_positions = [Position(pos.row - 1, pos.col), Position(pos.row, pos.col - 1), Position(pos.row + 1, pos.col), Position(pos.row, pos.col + 1)]
		for nb_pos in neighbor_positions:

			# Check if the neighboring position is off the board, which means the piece is being placed on the edge
			if not 0 <= nb_pos.row < len(board):
				continue
			if not 0 <= nb_pos.col < len(board[0]):
				continue

			# Check if there is an empty space nearby
			if board[nb_pos.row][nb_pos.col] is None:
				is_possible = True

			# Check if there is a piece of the same color nearby
			elif board[nb_pos.row][nb_pos.col].color == self.color:
				is_possible = True

		return is_possible

	def __eq__(self, other):
		'''
		Returns True if the two game piece objects are the same color

		Args:
			other (GamePiece): the other game piece object being compared to the current game piece

		'''
		return self.color == other.color

	def __str__(self):
		'''
		Returns the string representation of the game piece
		'''
		return f"{self.color} Piece"
