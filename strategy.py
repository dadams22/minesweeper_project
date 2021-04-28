from minesweeper_game import MinesweeperGame
from queue import PriorityQueue
import random


class ProbabilityAlgorithm:
    def __init__(self, game: MinesweeperGame):
        self.game = game

        self.open_list = []

        self.discovered_neighboring_bombs = [0] * (game.width * game.height)

    def play_game(self):
        starting_square = self.game.get_starting_square()
        self.open_list.append(starting_square)

        while not self.game.game_over():
            target_square = self._get_target_square()

            if target_square is None:
                covered_squares = self.game.get_covered_squares()
                square_to_uncover = random.choice(covered_squares)
                self._uncover_square(*square_to_uncover)
                continue

            covered_neighbors = self.game.get_covered_neighbors(*target_square)
            if len(covered_neighbors) == self._get_effective_label(*target_square):
                for neighbor in covered_neighbors:
                    self._flag_square(*neighbor)

                self.open_list.remove(target_square)
            else:
                square_to_uncover = random.choice(covered_neighbors)
                self._uncover_square(*square_to_uncover)

                if len(covered_neighbors) == 1 and target_square in self.open_list:
                    self.open_list.remove(target_square)

    def _uncover_square(self, x: int, y: int):
        label = self.game.uncover(x, y)
        if label == self.game.BOMB_LABEL:
            self._update_discovered_bomb_counts(x, y)
        else:
            self.open_list.append((x, y))

    def _flag_square(self, x: int, y: int):
        self.game.place_flag(x, y)
        self._update_discovered_bomb_counts(x, y)

    def _get_target_square(self):
        if self.open_list:
            target = max(self.open_list, key=lambda coord: self._bomb_probability(*coord))
            if self._bomb_probability(*target) > 0:
                return target
        return None

    def _update_discovered_bomb_counts(self, bomb_x: int, bomb_y: int):
        neighbors = self.game.get_neighbors(bomb_x, bomb_y)
        for neighbor in neighbors:
            self.discovered_neighboring_bombs[self._index(*neighbor)] += 1

    def _get_effective_label(self, x: int, y: int) -> int:
        return self.game.get_label(x, y) - self.discovered_neighboring_bombs[self._index(x, y)]

    def _bomb_probability(self, x: int, y: int) -> float:
        covered_neighbors = len(self.game.get_covered_neighbors(x, y))
        effective_label = self._get_effective_label(x, y)

        if effective_label == 0 or covered_neighbors == 0:
            return 0

        return effective_label / covered_neighbors

    def _index(self, x: int, y: int):
        return (y * self.game.width) + x
