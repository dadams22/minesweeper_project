from minesweeper_game import MinesweeperGame, load_game_from_file
from strategy import ProbabilityAlgorithm
from analysis import bomb_density_test, board_size_test


if __name__ == '__main__':
    bomb_density_test(ProbabilityAlgorithm)
    board_size_test(ProbabilityAlgorithm)