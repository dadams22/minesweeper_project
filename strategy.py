from .minesweeper_game import MinesweeperGame
from queue import PriorityQueue


class ProbabilityAlgorithm:
    def __init__(self, game: MinesweeperGame):
        self.game = game

        self.queue = PriorityQueue()

        self.discovered_neighboring_bombs = [0] * (self.width * self.height)

    def play_game(self):
        current_square = self.game.get_starting_square()
        while not self.game.game_over():
            covered_neighbors = self.game.get_covered_neighbors(*current_square)
            if self.get_effective_label(*current_square) == len(covered_neighbors):
                for neighbor in covered_neighbors:
                    self.game.place_flag(*neighbor)
                    self.discovered_neighboring_bombs[self._index(*neighbor)] += 1

    def get_effective_label(self, x, y):
        return self.game.get_label(x, y) - self.discovered_neighboring_bombs[self._index(x, y)]

    def _index(self, x: int, y: int):
        return (y * self.game.width) + x
