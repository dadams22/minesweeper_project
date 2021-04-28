from minesweeper_game import MinesweeperGame
from queue import PriorityQueue
import random


class ProbabilityAlgorithm:
    def __init__(self, game: MinesweeperGame):
        self.game = game

        self.queue = PriorityQueue()

        self.discovered_neighboring_bombs = [0] * (game.width * game.height)

    def play_game(self):
        starting_square = self.game.get_starting_square()
        current_square = None
        while not self.game.game_over():
            if current_square is None:
                covered_squares = self.game.get_covered_squares()
                self.game.uncover(*random.choice(covered_squares))

    def get_effective_label(self, x, y):
        return self.game.get_label(x, y) - self.discovered_neighboring_bombs[self._index(x, y)]

    def _index(self, x: int, y: int):
        return (y * self.game.width) + x
