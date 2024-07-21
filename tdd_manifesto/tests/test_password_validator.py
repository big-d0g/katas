import unittest

from tdd_manifesto.password_validator import password_validator


class TestPasswordValidator(unittest.TestCase):
    # Must be at least 8 characters long. If it is not met, then the following error
    # message should be returned: “Password must be at least 8 characters”
    def test_validator_should_return_error_for_input_less_than_eight_char(self) -> None:
        pw_input = "Te$t11"
        result = password_validator(pw_input)

        self.assertEqual(result, "Password must be at least 8 characters")

    # Must contain at least 2 numbers. If it is not met, then the following error message
    # should be returned: “The password must contain at least 2 numbers”
    def test_validator_should_return_error_when_input_not_containing_two_numbers(
        self,
    ) -> None:
        pw_input = "Te$t1test"
        result = password_validator(pw_input)

        self.assertEqual(result, "The password must contain at least 2 numbers")

    # Should handle multiple validation errors. E.G. “somepassword” should return:
    # “Password must be at least 8 characters\nThe password must contain at least 2 numbers”
    def test_validator_should_handle_multiple_validation_errors(self) -> None:
        pw_input = "Te$t1"
        result = password_validator(pw_input)

        self.assertEqual(
            result,
            "Password must be at least 8 characters\n"
            "The password must contain at least 2 numbers",
        )

    # Must contain at least one capital letter. If not met, should return:
    # “password must contain at least one capital letter”
    def test_validator_should_return_error_when_input_not_containing_capital(
        self,
    ) -> None:
        pw_input = "te$t1test1"
        result = password_validator(pw_input)

        self.assertEqual(result, "Password must contain at least one capital letter")

    # Must contain at least one special character. If it is not met, then should return:
    # “Password must contain at least one special character”
    def test_validator_should_return_error_when_input_not_containing_special_char(
        self,
    ) -> None:
        pw_input = "Test1test1"
        result = password_validator(pw_input)

        self.assertEqual(result, "Password must contain at least one special character")

    def test_validator_should_return_true_when_all_validations_met(self) -> None:
        pw_input = "Te$t1test1"
        result = password_validator(pw_input)

        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
