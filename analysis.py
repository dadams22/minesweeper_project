from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
from collections import defaultdict
from minesweeper_game import load_game_from_file


def get_all_files(directory_path: str):
    files = []
    for file in listdir(directory_path):
        full_filepath = join(directory_path, file)
        if isfile(full_filepath):
            files.append(full_filepath)
    return files


def board_density_test(algorithm):
    board_files = get_all_files('test_cases/test_boards/varied_density')

    squares_uncovered_by_density = defaultdict(list)

    for board_filepath in board_files:
        game = load_game_from_file(board_filepath)
        player = algorithm(game)
        player.play_game()

        density = game.bomb_count
        squares_uncovered = game.count_uncovered

        squares_uncovered_by_density[density].append(squares_uncovered)

    squares_uncovered_by_density = sorted(squares_uncovered_by_density.items(), key=lambda item: item[0])
    densities = []
    best = []
    worst = []
    mean = []
    for density, uncovered_list in squares_uncovered_by_density:
        densities.append(density)
        best.append(min(uncovered_list))
        worst.append(max(uncovered_list))
        mean.append(sum(uncovered_list) / len(uncovered_list))
    
    plt.plot(densities, best, label='Best Performance')
    plt.plot(densities, mean, label='Mean Performance')
    plt.plot(densities, worst, label='Worst Performance')
    plt.legend()
    plt.show()
