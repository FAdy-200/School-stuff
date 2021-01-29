# this file imports from supplement code and is meant to be located in the same folder
from minimax import find_best_move
from tictactoe import TTTBoard
from connectfour import C4Board
from board import Move, Board


def board_factory(game) -> Board:
    if game == 'tictactoe':
        return TTTBoard()
    else:
        return C4Board()


def get_player_move(board) -> Move:
    player_move: Move = Move(-1)
    while player_move not in board.legal_moves:
        play: int = int(input("Enter a legal square (0-8):"))
        player_move = Move(play)
    return player_move


def play(game, max_depth):
    board = board_factory(game)
    while True:
        human_move: Move = get_player_move(board)
        board = board.move(human_move)
        if board.is_win:
            print("Human wins!")
            break
        elif board.is_draw:
            print("Draw!")
            break
        computer_move: Move = find_best_move(board, max_depth)
        print(f"Computer move is {computer_move}")
        board = board.move(computer_move)
        print(board)
        if board.is_win:
            print("Computer wins!")
            break
        elif board.is_draw:
            print("Draw!")
            break


if __name__ == '__main__':
    game = input("choose game (tictactoe or c4): ")
    max_depth = 3
    play(game, max_depth)
