from enum import Enum
from dataclasses import dataclass
from typing import Self


class State(Enum):
    ON = 1
    OFF = 0


@dataclass
class Light:
    x: int
    y: int
    state: State


class ChristmasLights:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.grid = self.init_grid()

    def init_grid(self) -> list[Light]:
        return [Light(x, y, State.OFF) for x in range(self.x) for y in range(self.y)]

    def turn_on(self, x: tuple[int, int], y: tuple[int, int]) -> Self:
        for light in self.grid:
            if x[0] >= light.x >= x[1] and y[0] >= light.y >= y[1]:
                light.state = State.ON

        return self
    
    def turn_off(self, x: tuple[int, int], y: tuple[int, int]) -> Self:
        for light in self.grid:
            if x[0] >= light.x >= x[1] and y[0] >= light.y >= y[1]:
                light.state = State.OFF

        return self
        


lights = ChristmasLights(10, 10)
lights.turn_on((0, 0), (5, 5))

print(lights.grid)
