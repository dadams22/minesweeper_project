import matplotlib.pyplot as plt
from minesweeper_game import MinesweeperGame, load_game_from_file
from strategy import ProbabilityAlgorithm
from analysis import bomb_density_test, board_size_test, run_all_tests


if __name__ == '__main__':
    run_all_tests(ProbabilityAlgorithm)
    plt.show()
