from abc import ABC, abstractmethod
from accountant import Accountant
from date import Date
from typing import Optional

class Casino(ABC):
    DEFAULT_GAME_NUM = 0
    DEFAULT_DATE = Date()
    DEFAULT_ACCOUNTANT = Accountant()

    def __init__(self, game_number=DEFAULT_GAME_NUM, date=None, accountant=None):
        # Assign default instances if not provided
        date = date or Casino.DEFAULT_DATE
        accountant = accountant or Casino.DEFAULT_ACCOUNTANT

        self.game_number = game_number
        self.date = date
        self.accountant = accountant

    def set_game_number(self, game_number: int) -> bool:
        if game_number >= 0:
            self.game_number = game_number
            return True
        return False

    def set_date(self, date: Optional['Date']) -> bool:
        if date is not None:
            self.date = date
            return True
        return False

    def set_accountant(self, accountant: Optional['Accountant']) -> bool:
        if accountant is not None:
            self.accountant = accountant
            return True
        return False

    def set_all(self, game_number: int, date: Optional['Date'], accountant: Optional['Accountant']) -> bool:
        return (
            self.set_game_number(game_number) and
            self.set_date(date) and
            self.set_accountant(accountant)
        )

    def get_game_number(self) -> int:
        return self.game_number

    def get_date(self) -> Optional['Date']:
        return self.date

    def get_accountant(self) -> Optional['Accountant']:
        return self.accountant

    def __str__(self) -> str:
        date_str = str(self.date) if self.date else "No Date Provided"
        accountant_str = str(self.accountant) if self.accountant else "No Accountant Provided"
        return f"Casino Stats:\nGame Number: {self.game_number}\nDate: {date_str}\nAccountant:\n{accountant_str}"

    @abstractmethod
    def calculate_winnings(self):
        pass

    @abstractmethod
    def deal_cards(self):
        pass


# Example Usage
if __name__ == "__main__":
    # Example of initializing Date and Accountant as default instances
    class Date:
        def __str__(self):
            return "Default Date"

    class Accountant:
        def __str__(self):
            return "Default Accountant"

    # Assign the default instances for the Casino class
    Casino.DEFAULT_DATE = Date()
    Casino.DEFAULT_ACCOUNTANT = Accountant()

    # Create and display a default Casino instance
    default_casino = Casino()
    print(default_casino)