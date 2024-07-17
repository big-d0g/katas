import unittest

from christmas_lights.main import ChristmasLights, State, Light


class TestChristmasLights(unittest.TestCase):
    def test_create(self) -> None:
        lights = ChristmasLights(4, 4)
        print(lights)


