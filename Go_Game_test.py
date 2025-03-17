import unittest

from game_player import GamePlayer
from placeble import Placeble
from game_piece import GamePiece
from go_model import GoModel
from position import Position
from player_colors import PlayerColors


class GamePieceTest(unittest.TestCase):
    def test_game_piece_is_a_player_color(self): #1
        with self.assertRaises(TypeError):
            GamePiece(3)
    def test_position_is_a_Position(self): #2
        temp_game_piece = GamePiece(PlayerColors.BLACK)
        self.assertFalse(temp_game_piece.is_valid_placement(PlayerColors.BLACK, [[None]]))
    def test_place_off_board(self): #3
        temp_position = Position(5, 5)
        temp_game_piece = GamePiece(PlayerColors.BLACK)
        self.assertFalse(temp_game_piece.is_valid_placement(temp_position, [[None]]))
    def test_is_position_occupied(self): #4
        temp_position = Position(0, 0)
        temp_game_piece = GamePiece(PlayerColors.BLACK)
        self.assertFalse(temp_game_piece.is_valid_placement(temp_position, [[PlayerColors.WHITE]]))
    def test_empty_space_as_neighbor(self): #5
        temp_position = Position(1, 1)
        temp_game_piece = GamePiece(PlayerColors.BLACK)
        self.assertTrue(temp_game_piece.is_valid_placement(temp_position, [[None, None, None],[None, None, None],[None, None, None]]))
    def test_neighbor_is_your_piece(self): #6
        temp_position = Position(1, 1)
        temp_game_piece = GamePiece(PlayerColors.BLACK)
        temp_neighbor_piece = GamePiece(PlayerColors.BLACK)
        self.assertTrue(temp_game_piece.is_valid_placement(temp_position, [[None, None, None],[temp_neighbor_piece, None, None],[None, None, None]]))
    def test_pieces_same_color(self): #7
        temp_game_piece = GamePiece(PlayerColors.BLACK)
        temp_neighbor_piece = GamePiece(PlayerColors.BLACK)
        self.assertTrue(temp_game_piece == temp_neighbor_piece)

class GamePlayerTest(unittest.TestCase):
    def test_game_player_is_a_player_color(self): #8
        with self.assertRaises(TypeError):
            GamePlayer(3)
    def test_valid_player_color(self): #9
        # with self.assertRaises(ValueError):
        #     GamePlayer(PlayerColors)
        pass
    def test_capture_count_not_a_number(self): #10
        temp_capture_count = GamePlayer(PlayerColors.BLACK)
        with self.assertRaises(TypeError):
            temp_capture_count.capture_count = 'red'
    def test_capture_count_is_negative(self): #11
        temp_capture_count = GamePlayer(PlayerColors.BLACK)
        with self.assertRaises(ValueError):
            temp_capture_count.capture_count = -1
    def test_skip_count_not_a_number(self): #12
        temp_skip_count = GamePlayer(PlayerColors.BLACK)
        with self.assertRaises(TypeError):
            temp_skip_count.skip_count = 'red'
    def test_skip_count_is_negative(self): #13
        temp_skip_count = GamePlayer(PlayerColors.BLACK)
        with self.assertRaises(ValueError):
            temp_skip_count.skip_count = -1



# class GoModelTest(unittest.TestCase):
#     pass


if __name__ == '__main__':
    unittest.main()
