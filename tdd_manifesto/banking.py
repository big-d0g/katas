from dataclasses import asdict, dataclass, fields
from datetime import date
from typing import Protocol


class IAccount(Protocol):
    def deposit(self, amount: int) -> int: ...

    def withdraw(self, amount: int) -> int: ...

    def print_statement(self) -> str: ...


class Account:
    def __init__(self, balance: int = 0) -> None:
        self.balance: int = balance
        self._history: list[Transaction] = []

    def deposit(self, amount: int, date_: date = date.today()) -> None:
        self.balance += amount
        self._history.append(Transaction(date_, amount, self.balance))

    def withdraw(self, amount: int, date_: date = date.today()) -> None:
        self.balance += amount
        self._history.append(Transaction(date_, amount, self.balance))

    def print_statement(self) -> str:
        statement = [Transaction.headers()] + self._history
        formatted_statement = self._format_statement(statement)
        return formatted_statement

    @staticmethod
    def _format_statement(statement: list) -> str:
        if len(statement) == 1:
            return " | ".join(statement[0])

        formatted = []
        header = " | ".join(statement[0])
        formatted.append(header)

        for trx in statement[1:]:
            line = trx.print_transaction()
            formatted.append(" | ".join(line))

        return "\n".join(formatted)


@dataclass
class Transaction:
    entry_date: date
    amount: int
    balance: int | None

    @classmethod
    def headers(cls) -> list:
        headers: list = []
        for i in fields(cls):
            headers.append(i.name)

        return headers

    def print_transaction(self) -> list:
        trx = []
        for i in asdict(self).values():
            if isinstance(i, date):
                i = i.strftime("%d/%m/%Y")
            if isinstance(i, int):
                i = "%.2f" % i
            trx.append(i)

        return trx
