from enum import Enum
from dataclasses import dataclass
from typing import Self, TypeVar


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
        self.grid = self.create()

    def create(self) -> list[Light]:
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

    def toggle(self, x: tuple[int, int], y: tuple[int, int]) -> Self:
        for light in self.grid:
            if x[0] >= light.x >= x[1] and y[0] >= light.y >= y[1]:
                light.state = State.ON if light.state == State.OFF else State.OFF

        return self

    def count_lights(self, state: State) -> int:
        count = 0

        for light in self.grid:
            if light.state == state:
                count += 1

        return count

    @property
    def grid_info(self) -> dict[str, int]:
        return {
            "x": self.x,
            "y": self.y,
            "total_lights": self.x * self.y,
            "lights_on": self.count_lights(State.ON),
            "lights_off": self.count_lights(State.OFF),
        }


@dataclass
class LightV2:
    x: int
    y: int
    brightness: int


class ChristmasLightsV2:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.grid = self.create()

    def create(self) -> list[LightV2]:
        return [LightV2(x, y, 0) for x in range(self.x) for y in range(self.y)]

    def turn_on(self, x: tuple[int, int], y: tuple[int, int]) -> Self:
        for light in self.grid:
            if x[0] >= light.x >= x[1] and y[0] >= light.y >= y[1]:
                light.brightness += 1

        return self

    def turn_off(self, x: tuple[int, int], y: tuple[int, int]) -> Self:
        for light in self.grid:
            if x[0] >= light.x >= x[1] and y[0] >= light.y >= y[1]:
                light.brightness -= 1 if light.brightness > 0 else 0

        return self

    def toggle(self, x: tuple[int, int], y: tuple[int, int]) -> Self:
        for light in self.grid:
            if x[0] >= light.x >= x[1] and y[0] >= light.y >= y[1]:
                light.brightness += 2

        return self

    def count_brightness(self) -> int:
        count = 0

        for light in self.grid:
            count += light.brightness

        return count

    @property
    def grid_info(self) -> dict[str, int]:
        return {
            "x": self.x,
            "y": self.y,
            "total_brightness": self.count_brightness(),
        }


T = TypeVar("T", ChristmasLights, ChristmasLightsV2)


def santas_instructions(christmas_lights: T) -> T:
    christmas_lights.turn_on(x=(887, 9), y=(959, 629))
    christmas_lights.turn_on(x=(454, 398), y=(844, 448))
    christmas_lights.turn_off(x=(539, 243), y=(559, 965))
    christmas_lights.turn_off(x=(370, 819), y=(676, 868))
    christmas_lights.turn_off(x=(145, 40), y=(370, 997))
    christmas_lights.turn_off(x=(301, 3), y=(808, 453))
    christmas_lights.turn_on(x=(351, 678), y=(951, 908))
    christmas_lights.toggle(x=(720, 196), y=(897, 994))
    christmas_lights.toggle(x=(831, 394), y=(904, 860))

    return christmas_lights


if __name__ == "__main__":
    # Initialize the Christmas Lights
    lights = ChristmasLights(1000, 1000)
    start = lights.grid_info
    print(f"START: {start}")

    # Santa's Instructions
    lights = santas_instructions(lights)

    # Get the final state of the Christmas Lights
    end = lights.grid_info
    print(f"END: {end}")

    # After following Santa's instructions, how many lights are on?
    print(f"Lights On: {end['lights_on']}")
