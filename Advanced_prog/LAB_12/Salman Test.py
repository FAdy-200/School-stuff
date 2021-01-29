# this file imports from supplement code and is meant to be located in the same folder
import unittest
from random import randint
from tictactoe import TTTBoard
from connectfour import C4Board, C4Piece
from minimax import minimax  # NOQA


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.board = TTTBoard()

    def test_legal_moves(self):
        self.assertEqual(self.board.legal_moves, list(range(9)))
        n_moves = randint(0, 9)
        list_of_moves = list(range(9))
        # make random moves and test legal moves
        for i in range(n_moves):
            idx = randint(0, len(list_of_moves) - 1)
            position = list_of_moves[idx]
            self.board = self.board.move(position)
            del (list_of_moves[idx])
            self.assertEqual(self.board.legal_moves, list_of_moves)

    def test_win(self):
        # this is a win for X
        for move in [0, 1, 4, 2, 8]:
            self.assertFalse(self.board.is_win)
            self.board = self.board.move(move)
        self.assertTrue(self.board.is_win)

    def test_draw(self):
        def is_draw(board):
            return (not board.is_win) and (board.legal_moves == [])

        for move in [0, 1, 2, 3, 5, 8, 4, 6, 7]:
            self.assertFalse(is_draw(self.board))
            self.board = self.board.move(move)
        # The game is drawn now
        self.assertTrue(is_draw(self.board))


class TestMinMax(unittest.TestCase):
    def setUp(self):
        self.board = C4Board()

    def test_win_prevention(self):
        self.board = self.board.move(3)
        self.board = self.board.move(3)
        self.board = self.board.move(4)
        # In this position, black needs to occupy 2 or 5, otherwise black will occupy any of them
        # and win next move. This is actually harder than preventing a direct win.

        recommendation = minimax(self.board, maximizing=True, original_player=C4Piece.B,
                                 max_depth=4)
        self.assertIn(recommendation, [2, 5])

    def test_win_detection(self):
        self.board = self.board.move(0)
        self.board = self.board.move(1)
        self.board = self.board.move(0)
        self.board = self.board.move(1)
        self.board = self.board.move(0)
        self.board = self.board.move(1)

        # Red will win if played in 0

        recommendation = minimax(self.board, maximizing=True, original_player=C4Piece.B,
                                 max_depth=4)
        self.assertEqual(recommendation, 0)


x = TestMinMax()
x.setUp()
x.test_win_detection()
# unittest.main()
