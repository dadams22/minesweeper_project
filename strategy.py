from .minesweeper_game import MinesweeperGame
from queue import PriorityQueue


class ProbabilityAlgorithm:
    def __init__(self, game: MinesweeperGame):
        self.game = game

        self.queue = PriorityQueue()

        self.discovered_neighboring_bombs = [0] * (self.width * self.height)

    def get_effective_label(self, x, y):
        return self.game.get_label(x, y) - self.discovered_neighboring_bombs[self._index(x, y)]

    def _index(self, x: int, y: int):
        return (y * self.game.width) + x
