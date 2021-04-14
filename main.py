from minesweeper_game import MinesweeperGame


if __name__ == '__main__':
    game = MinesweeperGame('110001110000111', 5, 3)

    game.uncover(3, 0)

    print(str(game))
