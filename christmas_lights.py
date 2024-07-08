from enum import Enum

class State(Enum):
    ON = 1
    OFF = 0


class ChristmasLights:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.grid = self.init_grid

    def init_grid(self) -> list[tuple[int, int, State]]:
        return [(x, y, State.OFF) for x in range(self.x) for y in range(self.y)]
    