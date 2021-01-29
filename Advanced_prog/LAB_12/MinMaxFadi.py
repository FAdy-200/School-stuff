from tictactoe import TTTBoard

game = TTTBoard()


def minmax(board: TTTBoard, player, maxDepth=8):
    if maxDepth == 0 or board.evaluate(player):
        return board.evaluate(player)
    legal = board.legal_moves
    if player == "O":
        x = []
        for i in legal:
            x.append((minmax(board.move(i), "X", maxDepth=len(legal) - 1), i))
            # print(board)
        x = sorted(x, key=lambda x: x[0], reverse=False)
    else:
        x = []
        for i in legal:
            x.append((minmax(board.move(i), "O", maxDepth=len(legal) - 1), i))
            # print(board)
        x = sorted(x, key=lambda x: x[0], reverse=True)
    # print(c4t)
    for i in x:
        if i[1] in legal:
            return i[0]
    if len(x) == 0:
        if player == "O":
            return 100
        else:
            return -100


while not game.is_win:
    n = int(input())
    if n == 1:
        print()
        print()
    game = game.move(n)
    game = game.move(minmax(game, "O", maxDepth=len(game.legal_moves)-1))
    print(game)
    print(game.legal_moves)
