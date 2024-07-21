import unittest
from datetime import date

from tdd_manifesto.banking import Account, Transaction


class TestAccount(unittest.TestCase):
    def test_account_should_return_new_balance_when_deposit_made(self) -> None:
        amount = 1000
        account = Account()
        account.deposit(amount)

        self.assertEqual(account.balance, 1000)

    def test_account_should_return_new_balance_when_withdrawal_made(self) -> None:
        amount = -500
        account = Account()
        account.balance = 1000
        account.withdraw(amount)

        self.assertEqual(account.balance, 500)

    def test_account_print_statement_should_return_statement_headers(self) -> None:
        account = Account()
        trx_headers = Transaction.headers()
        result = account.print_statement()

        for i in trx_headers:
            self.assertIn(i, result)

    def test_account_print_statement_should_return_statement_with_trx_history(
        self,
    ) -> None:
        today_date = date.today().strftime("%d/%m/%Y")
        account = Account()
        deposit_amount = 1000
        withdrawal_amount = -100
        account.deposit(deposit_amount)
        account.withdraw(withdrawal_amount)
        new_balance = deposit_amount + withdrawal_amount

        result = account.print_statement()

        self.assertIn(today_date, result)
        self.assertIn(str(deposit_amount), result)
        self.assertIn(str(withdrawal_amount), result)
        self.assertIn(str(new_balance), result)


class TestTransaction(unittest.TestCase):
    def test_transaction_headers_should_return_list_of_headers(self) -> None:
        headers = Transaction.headers()

        self.assertEqual(headers, ["entry_date", "amount", "balance"])

    def test_transaction_print_transaction_should_return_list_of_transaction_values(
        self,
    ) -> None:
        today_date = date.today().strftime("%d/%m/%Y")
        trx = Transaction(date.today(), 1000, 1000)
        result = trx.print_transaction()

        self.assertIn(today_date, result)
        self.assertIn("1000.00", result)
        self.assertIn("1000.00", result)


if __name__ == "__main__":
    unittest.main()
