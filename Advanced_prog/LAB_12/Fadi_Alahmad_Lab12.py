# CSE314- Lab 12
#
# Topic: Artificial Intelligent Opponent For Board Games
# Author : Fadi Alahmad 120180049
# Date : 27/01/2021
# Question 1:
import unittest
import minimax
from random import randint
import connectfour
import tictactoe
from board import Move


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.board = tictactoe.TTTBoard()

    def test_legal_moves(self):
        self.assertEqual(self.board.legal_moves, list(range(9)))  # making sure that at first all moves are legal
        for i in range(9):  # performing 9 tests
            moves = self.board.legal_moves
            move = randint(0, len(moves) - 1)  # randomizing the move
            self.board = self.board.move(moves[move])
            moves.pop(move)
            self.assertEqual(self.board.legal_moves, moves)

    def test_win(self):
        z = [0, 1, 3, 4, 6]  # creating a win game
        for i in z:
            self.assertFalse(self.board.is_win)  # making sure the game is not won yet
            self.board = self.board.move(i)  # playing a move
        self.assertTrue(self.board.is_win)  # making sure the game is won

    def test_draw(self):
        # the ticktacktoe code did not have a is_draw function so i created one here
        def is_draw(board):
            if not board.is_win and len(board.legal_moves) == 0:
                return True
            return False

        z = [0, 1, 2, 3, 5, 4, 7, 8, 6]  # creating a draw game
        for i in z:
            self.assertFalse(is_draw(self.board))  # making sure the game is not a draw yet
            self.board = self.board.move(i)
        self.assertTrue(is_draw(self.board))  # making sure the game is a draw


# unittest.main()

# Question 2:
class TestMinMaxC4(unittest.TestCase):
    def setUp(self):
        self.board = connectfour.C4Board()

    # both tests fail as there something wrong with the algorithm provided
    def test_win_prevention(self):
        """
        testing to see if the ai play is the right one to prevent the other player from wining
        :return:
        """
        z = [0, 0, 1, 1, 2]  # the ai play must be 3 ot stop the other player from wining
        for i in z:
            self.board = self.board.move(i)
        aiPlay = minimax.minimax(self.board, maximizing=True, original_player=connectfour.C4Piece.B,
                                 max_depth=4)
        self.assertEqual(aiPlay, 3)

    def test_win_detection(self):
        z = [0, 0, 1, 1, 2, 2]  # black wins if plays in 3
        for i in z:
            self.board = self.board.move(i)
        aiPlay = minimax.minimax(self.board, maximizing=True, original_player=connectfour.C4Piece.B,
                                 max_depth=4)
        self.assertEqual(aiPlay, 3)


# unittest.main()


# question 3:


def get_player_move(board) -> Move:
    player_move: Move = Move(-1)
    while player_move not in board.legal_moves:
        play = int(input(f"Enter a legal play from {board.legal_moves}:"))
        player_move = Move(play)
    return player_move


def play(game):
    """
    :param game: game board of the desired game
    :return:
    """

    while True:
        playerMove = get_player_move(game)
        game = game.move(playerMove)
        if game.is_win:
            print("Human wins!")
            break
        elif game.is_draw:
            print("Draw!")
            break
        aiMove = minimax.find_best_move(game, 5)
        print(f"Computer move is {aiMove}")
        game = game.move(aiMove)
        print(game)
        if game.is_win:
            print("Computer wins!")
            break
        elif game.is_draw:
            print("Draw!")
            break

#
# gameToBePlayed = input("choose game t for TicTackToe c for Connect4: ")
# if gameToBePlayed == "t":
#     gamePlayed = tictactoe.TTTBoard()
# elif gameToBePlayed == "c":
#     gamePlayed = connectfour.C4Board()
# play(gamePlayed)
