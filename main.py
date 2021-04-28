from minesweeper_game import MinesweeperGame, load_game_from_file
from strategy import ProbabilityAlgorithm
from analysis import bomb_density_test, board_size_test


if __name__ == '__main__':
    print('Beginning Density Test')
    bomb_density_test(ProbabilityAlgorithm)
    print('Density Test Complete')

    print('Beginning Size Test')
    board_size_test(ProbabilityAlgorithm)
    print('Size Test Complete')
