from casino import Casino
from date import Date
import random


class Lottery(Casino):
    DEFAULT_TICKET_NUM = 1

    def __init__(self, game_number=Casino.DEFAULT_GAME_NUM, ticket_num=DEFAULT_TICKET_NUM, date=Casino.DEFAULT_DATE):
        super().__init__(game_number, date)
        self.ticket_num = ticket_num
        self.lotto_numbers = self.generate_lotto_numbers()
        self.user_selected = []

    def set_ticket_num(self, ticket_num: int) -> bool:
        if ticket_num > 0:
            self.ticket_num = ticket_num
            return True
        return False

    def get_ticket_num(self) -> int:
        return self.ticket_num

    def generate_lotto_numbers(self):
        return [random.randint(1, 50) for _ in range(6)]

    def set_user_selected(self, numbers: list[int]) -> bool:
        if len(numbers) == 6 and all(1 <= num <= 50 for num in numbers):
            self.user_selected = numbers
            return True
        return False

    def calculate_winnings(self) -> float:
        if not self.user_selected:
            raise ValueError("No user numbers selected.")
        matches = len(set(self.user_selected) & set(self.lotto_numbers))
        winnings = {6: 1_000_000, 5: 50_000, 4: 1_000, 3: 100, 2: 10, 1: 5, 0: 0}
        return winnings.get(matches, 0)

    def deal_cards(self):
        # Not applicable to Lottery, but required by the abstract Casino class
        pass

    def __str__(self) -> str:
        lotto_str = ", ".join(map(str, self.lotto_numbers))
        user_str = ", ".join(map(str, self.user_selected)) if self.user_selected else "No numbers selected"
        return (
            f"Lottery Stats:\n"
            f"Game Number: {self.game_number}\n"
            f"Ticket Number: {self.ticket_num}\n"
            f"Lotto Numbers: {lotto_str}\n"
            f"User Selected: {user_str}\n"
            f"Date: {self.date}\n"
            f"Accountant:\n{self.accountant}"
        )
