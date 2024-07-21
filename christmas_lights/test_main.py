import unittest

from christmas_lights.main import ChristmasLights, ChristmasLightsV2, State


class TestChristmasLights(unittest.TestCase):
    def test_init(self) -> None:
        lights = ChristmasLights(2, 2)

        self.assertTrue(isinstance(lights, ChristmasLights))
        self.assertEqual(lights.x, 2)
        self.assertEqual(lights.y, 2)
        self.assertEqual(len(lights.grid), 9)

    def test_turn_on(self) -> None:
        lights_1 = ChristmasLights(2, 2)

        lights_1.turn_on(start=(0, 0), end=(2, 2))
        total_on = [light for light in lights_1.grid if light.state == State.ON]

        self.assertEqual(len(total_on), 9)

        lights_2 = ChristmasLights(2, 2)
        lights_2.turn_on(start=(0, 0), end=(1, 1))
        total_on = [light for light in lights_2.grid if light.state == State.ON]

        self.assertEqual(len(total_on), 4)

        lights_3 = ChristmasLights(2, 2)
        lights_3.turn_on(start=(1, 1), end=(2, 2))
        total_on = [light for light in lights_3.grid if light.state == State.ON]

        self.assertEqual(len(total_on), 4)

    def test_turn_off(self) -> None:
        lights_1 = ChristmasLights(2, 2)
        lights_1.turn_on(start=(0, 0), end=(2, 2))

        lights_1.turn_off(start=(0, 0), end=(2, 2))
        total_off = [light for light in lights_1.grid if light.state == State.OFF]

        self.assertEqual(len(total_off), 9)

        lights_2 = ChristmasLights(2, 2)
        lights_2.turn_on(start=(0, 0), end=(2, 2))
        lights_2.turn_off(start=(0, 0), end=(1, 1))
        total_off = [light for light in lights_2.grid if light.state == State.OFF]

        self.assertEqual(len(total_off), 4)

        lights_3 = ChristmasLights(2, 2)
        lights_3.turn_on(start=(0, 0), end=(2, 2))
        lights_3.turn_off(start=(1, 1), end=(2, 2))
        total_off = [light for light in lights_3.grid if light.state == State.OFF]

        self.assertEqual(len(total_off), 4)

    def test_toggle(self) -> None:
        lights = ChristmasLights(2, 2)
        lights.toggle(start=(0, 0), end=(2, 2))

        total_on = [light for light in lights.grid if light.state == State.ON]
        self.assertEqual(len(total_on), 9)

        lights.toggle(start=(0, 0), end=(2, 2))
        total_on = [light for light in lights.grid if light.state == State.ON]
        self.assertEqual(len(total_on), 0)

        lights.toggle(start=(0, 0), end=(1, 1))
        total_on = [light for light in lights.grid if light.state == State.ON]

        self.assertEqual(len(total_on), 4)

        lights.toggle(start=(1, 1), end=(2, 2))
        total_on = [light for light in lights.grid if light.state == State.ON]

        self.assertEqual(len(total_on), 6)

        lights.toggle(start=(0, 0), end=(2, 2))
        total_on = [light for light in lights.grid if light.state == State.ON]

        self.assertEqual(len(total_on), 3)

    def test_count_lights(self) -> None:
        lights = ChristmasLights(2, 2)
        lights.turn_on(start=(0, 0), end=(2, 2))

        self.assertEqual(lights.count_lights(State.ON), 9)
        self.assertEqual(lights.count_lights(State.OFF), 0)

        lights.turn_off(start=(0, 0), end=(2, 2))

        self.assertEqual(lights.count_lights(State.ON), 0)
        self.assertEqual(lights.count_lights(State.OFF), 9)

        lights.turn_on(start=(0, 0), end=(1, 1))

        self.assertEqual(lights.count_lights(State.ON), 4)
        self.assertEqual(lights.count_lights(State.OFF), 5)

    def test_grid_info(self) -> None:
        lights = ChristmasLights(2, 2)

        self.assertEqual(
            lights.grid_info,
            {
                "x": 2,
                "y": 2,
                "total_lights": 9,
                "lights_on": 0,
                "lights_off": 9,
            },
        )

        lights.turn_on(start=(0, 0), end=(2, 2))

        self.assertEqual(
            lights.grid_info,
            {
                "x": 2,
                "y": 2,
                "total_lights": 9,
                "lights_on": 9,
                "lights_off": 0,
            },
        )

        lights.turn_off(start=(0, 0), end=(1, 1))

        self.assertEqual(
            lights.grid_info,
            {
                "x": 2,
                "y": 2,
                "total_lights": 9,
                "lights_on": 5,
                "lights_off": 4,
            },
        )


class TestChristmasLightsV2(unittest.TestCase):
    def test_init(self) -> None:
        lights = ChristmasLightsV2(2, 2)

        self.assertTrue(isinstance(lights, ChristmasLightsV2))
        self.assertEqual(lights.x, 2)
        self.assertEqual(lights.y, 2)
        self.assertEqual(len(lights.grid), 9)

    def test_turn_on(self) -> None:
        lights_1 = ChristmasLightsV2(2, 2)

        lights_1.turn_on(start=(0, 0), end=(2, 2))
        total_on = [light.brightness for light in lights_1.grid if light.brightness > 0]
        total_brightness = sum(total_on)

        self.assertEqual(total_brightness, 9)

        lights_2 = ChristmasLightsV2(2, 2)
        lights_2.turn_on(start=(0, 0), end=(1, 1))
        total_on = [light.brightness for light in lights_2.grid if light.brightness > 0]
        total_brightness = sum(total_on)

        self.assertEqual(total_brightness, 4)

        lights_3 = ChristmasLightsV2(2, 2)
        lights_3.turn_on(start=(1, 1), end=(2, 2))
        total_on = [light.brightness for light in lights_3.grid if light.brightness > 0]
        total_brightness = sum(total_on)

        self.assertEqual(total_brightness, 4)

        lights_3.turn_on(start=(0, 0), end=(2, 2))

        self.assertEqual(lights_3.count_brightness(), 13)

    def test_turn_off(self) -> None:
        lights_1 = ChristmasLightsV2(2, 2)
        lights_1.turn_on(start=(0, 0), end=(2, 2))

        lights_1.turn_off(start=(0, 0), end=(2, 2))
        total_off = [
            light.brightness for light in lights_1.grid if light.brightness > 0
        ]
        total_brightness = sum(total_off)

        self.assertEqual(total_brightness, 0)

        lights_2 = ChristmasLightsV2(2, 2)
        lights_2.turn_on(start=(0, 0), end=(2, 2))
        lights_2.turn_off(start=(0, 0), end=(1, 1))
        total_off = [
            light.brightness for light in lights_2.grid if light.brightness > 0
        ]
        total_brightness = sum(total_off)

        self.assertEqual(total_brightness, 5)

        lights_3 = ChristmasLightsV2(2, 2)
        lights_3.turn_on(start=(0, 0), end=(2, 2))
        lights_3.turn_off(start=(1, 1), end=(2, 2))
        lights_3.turn_on(start=(0, 0), end=(2, 2))
        lights_3.turn_on(start=(0, 0), end=(2, 2))
        lights_3.turn_off(start=(2, 2), end=(2, 2))
        total_off = [
            light.brightness for light in lights_3.grid if light.brightness > 0
        ]
        total_brightness = sum(total_off)

        self.assertEqual(total_brightness, 22)

    def test_toggle(self) -> None:
        lights = ChristmasLightsV2(2, 2)
        lights.toggle(start=(0, 0), end=(2, 2))

        total_on = [light.brightness for light in lights.grid if light.brightness > 0]
        total_brightness = sum(total_on)

        self.assertEqual(total_brightness, 18)

        lights.toggle(start=(1, 1), end=(2, 2))
        total_on = [light.brightness for light in lights.grid if light.brightness > 0]
        total_brightness = sum(total_on)

        self.assertEqual(total_brightness, 26)

        lights.toggle(start=(0, 0), end=(9, 9))
        total_on = [light.brightness for light in lights.grid if light.brightness > 0]
        total_brightness = sum(total_on)

        self.assertEqual(total_brightness, 44)

    def test_count_brightness(self) -> None:
        lights = ChristmasLightsV2(2, 2)
        lights.turn_on(start=(0, 0), end=(2, 2))

        self.assertEqual(lights.count_brightness(), 9)

        lights.toggle(start=(0, 0), end=(2, 2))

        self.assertEqual(lights.count_brightness(), 27)

        lights.turn_off(start=(0, 0), end=(1, 1))

        self.assertEqual(lights.count_brightness(), 23)

    def test_grid_info(self) -> None:
        lights = ChristmasLightsV2(2, 2)

        self.assertEqual(
            lights.grid_info,
            {
                "x": 2,
                "y": 2,
                "total_lights": 9,
                "total_brightness": 0,
            },
        )

        lights.turn_on(start=(0, 0), end=(2, 2))

        self.assertEqual(
            lights.grid_info,
            {
                "x": 2,
                "y": 2,
                "total_lights": 9,
                "total_brightness": 9,
            },
        )

        lights.turn_off(start=(0, 0), end=(1, 1))

        self.assertEqual(
            lights.grid_info,
            {
                "x": 2,
                "y": 2,
                "total_lights": 9,
                "total_brightness": 5,
            },
        )

        lights.toggle(start=(0, 0), end=(2, 2))

        self.assertEqual(
            lights.grid_info,
            {
                "x": 2,
                "y": 2,
                "total_lights": 9,
                "total_brightness": 23,
            },
        )
