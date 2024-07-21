from dataclasses import dataclass
from enum import Enum
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
        self.grid = [
            Light(x, y, State.OFF) for x in range(self.x + 1) for y in range(self.y + 1)
        ]

    def turn_on(self, start: tuple[int, int], end: tuple[int, int]) -> Self:
        for light in self.grid:
            if light.x >= start[0] and light.x <= end[0]:
                if light.y >= start[1] and light.y <= end[1]:
                    light.state = State.ON

        return self

    def turn_off(self, start: tuple[int, int], end: tuple[int, int]) -> Self:
        for light in self.grid:
            if light.x >= start[0] and light.x <= end[0]:
                if light.y >= start[1] and light.y <= end[1]:
                    light.state = State.OFF

        return self

    def toggle(self, start: tuple[int, int], end: tuple[int, int]) -> Self:
        for light in self.grid:
            if light.x >= start[0] and light.x <= end[0]:
                if light.y >= start[1] and light.y <= end[1]:
                    if light.state == State.ON:
                        light.state = State.OFF
                    else:
                        light.state = State.ON

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
            "total_lights": len(self.grid),
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
        return [LightV2(x, y, 0) for x in range(self.x + 1) for y in range(self.y + 1)]

    def turn_on(self, start: tuple[int, int], end: tuple[int, int]) -> Self:
        for light in self.grid:
            if light.x >= start[0] and light.x <= end[0]:
                if light.y >= start[1] and light.y <= end[1]:
                    light.brightness += 1

        return self

    def turn_off(self, start: tuple[int, int], end: tuple[int, int]) -> Self:
        for light in self.grid:
            if light.x >= start[0] and light.x <= end[0]:
                if light.y >= start[1] and light.y <= end[1]:
                    if light.brightness > 0:
                        light.brightness -= 1

        return self

    def toggle(self, start: tuple[int, int], end: tuple[int, int]) -> Self:
        for light in self.grid:
            if light.x >= start[0] and light.x <= end[0]:
                if light.y >= start[1] and light.y <= end[1]:
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
            "total_lights": len(self.grid),
            "total_brightness": self.count_brightness(),
        }


T = TypeVar("T", ChristmasLights, ChristmasLightsV2)


def santas_instructions(christmas_lights: T) -> T:
    christmas_lights.turn_on(start=(887, 9), end=(959, 629))
    christmas_lights.turn_on(start=(454, 398), end=(844, 448))
    christmas_lights.turn_off(start=(539, 243), end=(559, 965))
    christmas_lights.turn_off(start=(370, 819), end=(676, 868))
    christmas_lights.turn_off(start=(145, 40), end=(370, 997))
    christmas_lights.turn_off(start=(301, 3), end=(808, 453))
    christmas_lights.turn_on(start=(351, 678), end=(951, 908))
    christmas_lights.toggle(start=(720, 196), end=(897, 994))
    christmas_lights.toggle(start=(831, 394), end=(904, 860))

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

    # Initialize the Christmas Lights V2
    lights_v2 = ChristmasLightsV2(1000, 1000)
    start_v2 = lights_v2.grid_info
    print(f"START V2: {start_v2}")

    # Santa's Instructions
    lights_v2 = santas_instructions(lights_v2)

    # Get the final state of the Christmas Lights V2
    end_v2 = lights_v2.grid_info
    print(f"END V2: {end_v2}")

    # After following Santa's instructions, what is the total brightness of the lights?
    print(f"Total Brightness: {end_v2['total_brightness']}")
