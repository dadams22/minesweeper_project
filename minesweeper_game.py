import json
from typing import List


class MinesweeperGame:
    BOMB_LABEL = -1
    
    def __init__(self, bombs: List[bool], width: int, height: int, debug=False):
        self.width = width
        self.height = height
        self.DEBUG = debug

        self.bombs = bombs
        self.bomb_count = self.bombs.count(True)
        self.discovered_bomb_count = 0

        self.covered = [True] * (width * height)
        self.count_uncovered = 0

        self.labels = []
        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.get_neighbors(x, y)
                label = [self.is_bomb(*neighbor) for neighbor in neighbors].count(True)
                self.labels.append(label)

        self.flags = []

    def get_starting_square(self):
        if self.count_uncovered > 0:
            raise RuntimeError('The game has already started - starting square cannot be returned.')

        starting_square = None
        for x in range(self.width):
            for y in range(self.height):
                if self.is_bomb(x, y):
                    continue
                if starting_square is None or self.get_label(x, y) > self.get_label(*starting_square):
                    starting_square = (x, y)

        self.uncover(*starting_square)
        return starting_square

    def is_covered(self, x: int, y: int):
        return self.covered[self._index(x, y)]

    def uncover(self, x: int, y: int):
        self.covered[self._index(x, y)] = False
        self.count_uncovered += 1

        if self.is_bomb(x, y):
            self.place_flag(x, y)
            return self.BOMB_LABEL
        else:
            self._print_board()
            return self.get_label(x, y)

    def is_bomb(self, x: int, y: int):
        return self.bombs[self._index(x, y)]

    def get_neighbors(self, x: int, y: int):
        neighbor_translations = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1),
        ]

        neighbor_coords = []
        for x_shift, y_shift in neighbor_translations:
            new_x = x + x_shift
            new_y = y + y_shift
            if 0 <= new_x < self.width and 0 <= new_y < self.height:
                neighbor_coords.append((new_x, new_y))

        return neighbor_coords

    def get_covered_neighbors(self, x: int, y: int):
        return [
            neighbor for neighbor in self.get_neighbors(x, y)
            if self.is_covered(*neighbor)
        ]

    def get_uncovered_neighbors(self, x: int, y: int):
        return [
            neighbor for neighbor in self.get_neighbors(x, y)
            if not self.is_covered(*neighbor)
        ]

    def get_label(self, x: int, y: int):
        return self.labels[self._index(x, y)]

    def place_flag(self, x: int, y: int):
        if not self.is_bomb(x, y):
            raise ValueError('The square at (%d, %d) does not contain a bomb' % (x, y))
        if (x, y) in self.flags:
            raise ValueError('The square at (%d, %d) is already flagged' % (x, y))

        self.flags.append((x, y))
        self.covered[self._index(x, y)] = False
        self.discovered_bomb_count += 1

        self._print_board()

    def is_flagged(self, x, y):
        return (x, y) in self.flags

    def game_over(self) -> bool:
        if self.discovered_bomb_count == self.bomb_count:
            if self.DEBUG:
                print(
                    '\nGame Over - %d tiles uncovered, %d bombs found'
                    % (self.count_uncovered, self.discovered_bomb_count)
                )
            return True
        else:
            return False

    def get_covered_squares(self):
        covered_squares = []
        for x in range(self.width):
            for y in range(self.height):
                if self.is_covered(x, y):
                    covered_squares.append((x, y))
        return covered_squares

    def _print_board(self):
        if self.DEBUG:
            print('\n' + str(self) + '\n')

    def _index(self, x: int, y: int):
        return (y * self.width) + x

    def __str__(self):
        rows = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if self.is_flagged(x, y):
                    row.append(' F ')
                elif self.is_covered(x, y):
                    row.append('   ')
                elif self.is_bomb(x, y):
                    row.append(' * ')
                else:
                    bomb_count = self.get_label(x, y)
                    row.append(' %d ' % bomb_count)
            rows.append(row)

        rows = ['|'.join(row) for row in rows]
        return '\n'.join(rows)


def load_game_from_file(filepath: str) -> MinesweeperGame:
    with open(filepath, 'r') as board_file:
        board_data = json.load(board_file)

    board = board_data['board']
    bombs = [square == '9' for square in board]

    height, width = [int(dim) for dim in board_data['dim'].split(',')]
    return MinesweeperGame(bombs, width, height)
