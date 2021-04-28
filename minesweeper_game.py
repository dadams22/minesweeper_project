class MinesweeperGame:
    def __init__(self, bombs: str, width: int, height: int):
        self.width = width
        self.height = height

        self.bombs = [bomb == '1' for bomb in bombs]
        self.bomb_count = self.bombs.count(True)

        self.covered = [True] * (width * height)
        self.count_uncovered = 0

        self.bomb_counts = []
        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.get_neighbors(x, y)
                bomb_count = [self.is_bomb(*neighbor) for neighbor in neighbors].count(True)
                self.bomb_counts.append(bomb_count)

        self.flags = []

    def get_starting_square(self):
        if self.count_uncovered > 0:
            raise RuntimeError('The game has already started - starting square cannot be returned.')

        starting_square = None
        for x in range(self.width):
            for y in range(self.height):
                # print(x, y, self.is_bomb(x, y), self.get_bomb_count(x, y))
                if self.is_bomb(x, y):
                    continue
                if starting_square is None or self.get_bomb_count(x, y) > self.get_bomb_count(*starting_square):
                    starting_square = (x, y)

        self.uncover(*starting_square)
        return starting_square

    def is_covered(self, x: int, y: int):
        return self.covered[self._index(x, y)]

    def uncover(self, x: int, y: int):
        self.covered[self._index(x, y)] = False

        if self.is_bomb(x, y):
            self.place_flag(x, y)
            return -1
        else:
            return self.get_bomb_count(x, y)

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

    def get_bomb_count(self, x: int, y: int):
        return self.bomb_counts[self._index(x, y)]

    def place_flag(self, x: int, y: int):
        if not self.is_bomb(x, y):
            raise ValueError('The square at (%d, %d) does not contain a bomb' % (x, y))
        if (x, y) in self.flags:
            raise ValueError('The square at (%d, %d) is already flagged' % (x, y))

        self.flags.append((x, y))
        self.covered[self._index(x, y)] = False

    def is_flagged(self, x, y):
        return (x, y) in self.flags

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
                    bomb_count = self.get_bomb_count(x, y)
                    row.append(' %d ' % bomb_count)
            rows.append(row)

        rows = ['|'.join(row) for row in rows]
        return '\n'.join(rows)
