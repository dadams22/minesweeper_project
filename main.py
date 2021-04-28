from minesweeper_game import MinesweeperGame


if __name__ == '__main__':
    game = MinesweeperGame('110001110000111', 5, 3)

    print(game.get_starting_square())

    game.place_flag(0, 0)

    game.place_flag(0, 3)

    print(str(game))
