class MinesweeperGame:
    def __init__(self, bombs: str, width: int, height: int):
        self.width = width
        self.height = height

        self.bombs = [bomb == '1' for bomb in bombs]
        self.bomb_count = self.bombs.count(True)

        self.covered = [True] * (width * height)
        self.count_uncovered = 0

        self.neighboring_bomb_counts = []
        for y in range(self.height):
            for x in range(self.width):
                neighbors = self._generate_neighbor_coords(x, y)
                bomb_count = [self.is_bomb(*neighbor) for neighbor in neighbors].count(True)
                self.neighboring_bomb_counts.append(bomb_count)

        self.flags = []

    def is_covered(self, x: int, y: int):
        return self.covered[self._index(x, y)]

    def uncover(self, x: int, y: int):
        self.covered[self._index(x, y)] = False
        self.count_uncovered += 1

        if self.is_bomb(x, y):
            self.place_flag(x, y)
            return -1
        else:
            return self.get_neighboring_bomb_count(x, y)

    def is_bomb(self, x: int, y: int):
        return self.bombs[self._index(x, y)]

    def get_covered_neighbors(self, x: int, y: int):
        return [
            neighbor for neighbor in self._generate_neighbor_coords(x, y)
            if self.is_covered(*neighbor)
        ]

    def get_neighboring_bomb_count(self, x: int, y: int):
        if self.is_covered(x, y):
            raise ValueError(
                'The square at (%d, %d) is covered, so you cannot access its neighboring bomb count' % (x, y)
            )

        return self.neighboring_bomb_counts[self._index(x, y)]

    def place_flag(self, x: int, y: int):
        if not self.is_bomb(x, y):
            raise ValueError('The square at (%d, %d) does not contain a bomb' % (x, y))
        if (x, y) in self.flags:
            raise ValueError('The square at (%d, %d) is already flagged' % (x, y))

        self.flags.append((x, y))

    def _generate_neighbor_coords(self, x: int, y: int):
        neighbor_translations = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1),
        ]

        neighbor_coords = []
        for x_shift, y_shift in neighbor_translations:
            new_x = x + x_shift
            new_y = y + y_shift
            if 0 < new_x < self.width and 0 < new_y < self.height:
                neighbor_coords.append((x, y))

        return neighbor_coords

    def _index(self, x: int, y: int):
        return (y * self.width) + x

    def __str__(self):
        rows = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if self.is_covered(x, y):
                    row.append('   ')
                elif self.is_bomb(x, y):
                    row.append(' * ')
                else:
                    bomb_count = self.get_neighboring_bomb_count(x, y)
                    row.append(' %d ' % bomb_count)
            rows.append(row)

        rows = ['|'.join(row) for row in rows]
        return '\n'.join(rows)
