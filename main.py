from minesweeper_game import MinesweeperGame
from strategy import ProbabilityAlgorithm


if __name__ == '__main__':
    game = MinesweeperGame('110001110000111', 5, 3)

    minesweeper_player = ProbabilityAlgorithm(game)
    minesweeper_player.play_game()
