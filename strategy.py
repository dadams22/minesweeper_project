from .minesweeper_game import MinesweeperGame
from queue import PriorityQueue


class ProbabilityAlgorithm:
    def __init__(self, game: MinesweeperGame):
        self.game = game

        self.queue = PriorityQueue()