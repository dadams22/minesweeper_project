

class MinesweeperGame:
    def __init__(self, bombs: str, width: int, height: int):
        self.bombs = [bomb == '1' for bomb in bombs]
        self.covered = [True] * (width * height)