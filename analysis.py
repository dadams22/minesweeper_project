from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
from collections import defaultdict
from typing import Dict
from minesweeper_game import load_game_from_file
from timeit import default_timer as timer


def get_all_files(directory_path: str):
    files = []
    for file in listdir(directory_path):
        full_filepath = join(directory_path, file)
        if isfile(full_filepath):
            files.append(full_filepath)
    return files


def run_test(algorithm, test_boards_directory: str, get_x, x_label: str, axs):
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

    generate_performance_plot(runtimes_by_x_value, x_label, 'Runtime (s)', axs[0])
    generate_performance_plot(squares_uncovered_by_x_value, x_label, 'Squares Uncovered', axs[1])


def bomb_density_test(algorithm, axs):
    run_test(algorithm, 'test_cases/test_boards/varied_density', lambda game: game.bomb_count, 'Bomb Density', axs)


def board_size_test(algorithm, axs):
    run_test(algorithm, 'test_cases/test_boards/varied_size', lambda game: game.height * game.width, 'Board Size', axs)


def run_all_tests(algorithm):
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))

    bomb_density_test(algorithm, axs[0])
    board_size_test(algorithm, axs[1])


def generate_performance_plot(data: Dict, x_label: str, y_label: str, ax: plt.subplot):
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

    ax.plot(x, y_best, label='Best %s' % y_label, color='g')
    ax.plot(x, y_mean, label='Mean %s' % y_label, color='b')
    ax.plot(x, y_worst, label='Worst %s' % y_label, color='r')
    ax.set_title('%s vs. %s' % (y_label, x_label))
    ax.legend()
