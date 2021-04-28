from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
from collections import defaultdict
from typing import Dict
from minesweeper_game import MinesweeperGame, load_game_from_file
from timeit import default_timer as timer


def get_all_files(directory_path: str):
    files = []
    for file in listdir(directory_path):
        full_filepath = join(directory_path, file)
        if isfile(full_filepath):
            files.append(full_filepath)
    return files


def run_test(algorithm, test_boards_directory: str, x_label: str, get_x):
    board_files = get_all_files(test_boards_directory)

    squares_uncovered_by_x_value = defaultdict(list)
    runtimes_by_x_value = defaultdict(list)

    for board_filepath in board_files:
        game = load_game_from_file(board_filepath)
        player = algorithm(game)

        start_time = timer()
        player.play_game()
        end_time = timer()

        runtime = end_time - start_time
        squares_uncovered = game.count_uncovered
        x_value = get_x(game)

        runtimes_by_x_value[x_value].append(runtime)
        squares_uncovered_by_x_value[x_value].append(squares_uncovered)

    generate_performance_plot(runtimes_by_x_value, x_label, 'Runtime (s)')
    generate_performance_plot(squares_uncovered_by_x_value, x_label, 'Squares Uncovered')


def board_density_test(algorithm):
    run_test(algorithm, 'test_cases/test_boards/varied_density', 'Bomb Density', lambda game: game.bomb_count)


def generate_performance_plot(data: Dict, x_label: str, y_label: str):
    sorted_data = sorted(data.items(), key=lambda item: item[0])
    x = []
    y_best = []
    y_worst = []
    y_mean = []
    for x_value, y_values in sorted_data:
        x.append(x_value)
        y_best.append(min(y_values))
        y_worst.append(max(y_values))
        y_mean.append(sum(y_values) / len(y_values))

    plt.plot(x, y_best, label='Best %s' % y_label, color='g')
    plt.plot(x, y_mean, label='Mean %s' % y_label, color='b')
    plt.plot(x, y_worst, label='Worst %s' % y_label, color='r')
    plt.title('%s vs. %s' % (y_label, x_label))
    plt.legend()
    plt.show()
