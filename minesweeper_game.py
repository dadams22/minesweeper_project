

class MinesweeperGame:
    def __init__(self, bombs: str, width: int, height: int):
        self.width = width
        self.height = height

        self.bombs = [bomb == '1' for bomb in bombs]
        self.covered = [True] * (width * height)

        self.neighboring_bomb_counts = []
        for y in range(self.height):
            for x in range(self.width):
                neighbors = self._generate_neighbor_coords(x, y)
                bomb_count = [self.is_bomb(*neighbor) for neighbor in neighbors].count(True)
                self.neighboring_bomb_counts.append(bomb_count)

    def is_covered(self, x: int, y: int):
        return self.covered[self._index(x, y)]

    def uncover(self, x: int, y: int):
        self.covered[self._index(x, y)] = False

    def is_bomb(self, x: int, y: int):
        return self.bombs[self._index(x, y)]

    def get_covered_neighbors(self, x: int, y: int):
        return [
            neighbor for neighbor in self._generate_neighbor_coords(x, y)
            if self.is_covered(*neighbor)
        ]

    def get_neighboring_bomb_count(self, x: int, y: int):
        return self.neighboring_bomb_counts[self._index(x, y)]

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
                    row.append(' 0 ')
            rows.append(row)

        rows = ['|'.join(row) for row in rows]
        return '\n'.join(rows)
