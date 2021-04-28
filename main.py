from minesweeper_game import MinesweeperGame, load_game_from_file
from strategy import ProbabilityAlgorithm
from analysis import board_density_test


if __name__ == '__main__':
    # game = load_game_from_file('test_cases/test_boards/varied_density/20_20_2_0.json')
    #
    # minesweeper_player = ProbabilityAlgorithm(game)
    # minesweeper_player.play_game()

    board_density_test(ProbabilityAlgorithm)