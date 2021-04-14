

class MinesweeperGame:
    def __init__(self, bombs: str, width: int, height: int):
        self.width = width
        self.height = height

        self.bombs = [bomb == '1' for bomb in bombs]
        self.covered = [True] * (width * height)

    def is_covered(self, x, y):
        return self.covered[self._index(x, y)]

    def _index(self, x: int, y: int):
        return (y * self.height) + x
