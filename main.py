from minesweeper_game import MinesweeperGame


if __name__ == '__main__':
    game = MinesweeperGame('111111111111111', 5, 3)

    game.uncover(1, 1)

    print(str(game))