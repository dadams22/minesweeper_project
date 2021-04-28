from minesweeper_game import MinesweeperGame


if __name__ == '__main__':
    game = MinesweeperGame('110001110000111', 5, 3)

    starting_square = game.get_starting_square()
    print(starting_square)

    print(str(game))
