import player_colors
from game_piece import GamePiece
from go_model import GoModel
from player_colors import PlayerColors
from position import Position

b = PlayerColors.BLACK
w = PlayerColors.WHITE

board = [[None,         None,       None,           None,           None,           None],
         [None,         None,       None,           GamePiece(b),   None,           None],
         [None,         None,       GamePiece(w),   None,           GamePiece(w),   None],
         [None,         None,       None,           GamePiece(w),   None,           None],
         [None,         None,       None,           None,           None,           None],
         [None,         None,       None,           None,           None,           None]]

board2= [[None,         None,       None,           None,           None,           None],
         [None,         None,       None,           GamePiece(b),   None,           None],
         [None,         None,       GamePiece(w),   None,           GamePiece(w),   None],
         [None,         None,       None,           GamePiece(w),   None,           None],
         [None,         None,       None,           None,           None,           None],
         [None,         None,       None,           None,           None,           None]]


x = GoModel()
x.set_piece(Position(1, 3), GamePiece(b))
x.set_next_player()
x.set_piece(Position(3, 3), GamePiece(w))
x.set_next_player()
x.set_piece(Position(2, 2), GamePiece(w))
x.set_next_player()
x.set_piece(Position(2, 4), GamePiece(w))

print(x.is_same_board(board, board2))
