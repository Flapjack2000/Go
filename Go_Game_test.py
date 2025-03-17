import unittest
from placeble import Placeble
from game_piece import GamePiece
from go_model import GoModel
from position import Position
from player_colors import PlayerColors


class PlacebleTest(unittest.TestCase):
    def test_color_is_a_Player_Color(self): #1
        with self.assertRaises(TypeError):
            Placeble(-3)


class GamePieceTest(unittest.TestCase):
    def test_game_piece_is_a_player_color(self): #2
        with self.assertRaises(TypeError):
            GamePiece(3)
    def test_position_is_a_Position(self): #3
        temp_game_piece = GamePiece(PlayerColors.BLACK)
        self.assertFalse(temp_game_piece.is_valid_placement(PlayerColors.BLACK, [[None]]))
    def test_place_off_board(self): #4
        temp_position = Position(5, 5)
        temp_game_piece = GamePiece(PlayerColors.BLACK)
        self.assertFalse(temp_game_piece.is_valid_placement(temp_position, [[None]]))
    def test_is_position_occupied(self): #5
        temp_position = Position(0, 0)
        temp_game_piece = GamePiece(PlayerColors.BLACK)
        self.assertFalse(temp_game_piece.is_valid_placement(temp_position, [[PlayerColors.WHITE]]))
    def test_empty_space_as_neighbor(self):
        pass

# class GoModelTest(unittest.TestCase):
#     pass


if __name__ == '__main__':
    unittest.main()
