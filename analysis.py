from os import listdir
from os.path import isfile, join
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
