import unittest

from tdd_manifesto.string_calculator import add


class TestStringCalculator(unittest.TestCase):
    # Create a simple add that takes a String and returns an integer
    # The method can take up to two numbers, separated by commas, and will
    # return their sum as a result. So the inputs can
    # be: “”, “1”, “1,2”. For an empty string, it will return 0.
    def test_add_method_returns_sum_as_int_when_given_two_nums_as_str(self) -> None:
        str_nums = "2,4"
        result = add(str_nums)

        self.assertEqual(result, 6)

    def test_add_method_returns_int_if_one_num_is_given(self) -> None:
        str_nums = "2"
        result = add(str_nums)

        self.assertEqual(result, 2)

    def test_add_method_returns_zero_if_str_is_empty(self) -> None:
        str_nums = ""
        result = add(str_nums)

        self.assertEqual(result, 0)

    # Allow the add method to handle an unknown number of arguments
    def test_add_method_can_return_sum_of_any_number_of_args(self) -> None:
        str_num1 = "2"
        str_num2 = "4"
        result = add(str_num1, str_num2)

        self.assertEqual(result, 6)

    # Allow the add method to handle newlines as separators, instead of comas
    def test_add_method_returns_sum_with_newline_used_as_separator(self) -> None:
        str_num = "1,2\n3"
        result = add(str_num)

        self.assertEqual(result, 6)

    # Add validation not to allow a separator at the end
    def test_add_method_throws_error_if_num_string_ends_with_separator(self) -> None:
        str_num = "1,2,"

        with self.assertRaises(ValueError):
            add(str_num)

    def test_add_method_handles_different_delimiters(self) -> None:
        str_num1 = "//;\n1;3"
        str_num2 = "//|\n1|2|3"
        str_num3 = "//sep\n2sep5"

        self.assertEqual(add(str_num1), 4)
        self.assertEqual(add(str_num2), 6)
        self.assertEqual(add(str_num3), 7)


if __name__ == "__main__":
    unittest.main()
