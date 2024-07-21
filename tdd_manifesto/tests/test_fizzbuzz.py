import unittest

from tdd_manifesto.fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    # Write a “fizzBuzz” method that accepts a number as input and returns it as a String
    def test_fizzbuzz_method_accepts_number_and_returns_as_string(self) -> None:
        num = 1
        result = fizzbuzz(num)

        assert result == "1"

    # For multiples of three return “Fizz” instead of the number
    def test_fizzbuzz_returns_fizz_if_multiple_of_three(self) -> None:
        num = 6
        result = fizzbuzz(num)

        assert result == "Fizz"

    # For the multiples of five return “Buzz”
    def test_fizzbuzz_returns_buzz_if_multiple_of_five(self) -> None:
        num = 10
        result = fizzbuzz(num)

        assert result == "Buzz"

    # For numbers that are multiples of both three and five return “FizzBuzz”.
    def test_fizzbuzz_returns_fizzbuzz_if_multiple_of_three_and_five(self) -> None:
        num = 15
        result = fizzbuzz(num)

        assert result == "FizzBuzz"


if __name__ == "__main__":
    unittest.main()
