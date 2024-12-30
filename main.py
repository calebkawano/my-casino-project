from random import randint
from casino import Casino
from accountant import Accountant
from date import Date
from lottery import Lottery

class CasinoTester:
    def test_to_string(self):
        print("Testing casino's string representation...")
        casino_instance = Casino(1, Date("March", 15, 2024), Accountant(1000, 500, 500, 2))
        print(casino_instance)
        # Expected output:
        # Casino Stats:
        # Game Number: 1
        # Date: March 15, 2024
        # Accountant:
        # Money In: 1000, Money Out: 500, Total Money: 500, Transactions: 2

    def test_accountant(self):
        print("Testing Accountant...")
        accountant_instance = Accountant(2000, 1500, 500, 3)
        print(accountant_instance)
        # Expected output:
        # Money In: 2000, Money Out: 1500, Total Money: 500, Transactions: 3

    def test_to_string_date(self):
        print("Testing date's string representation...")
        date_instance = Date("February", 28, 2022)
        print(date_instance)
        # Expected output:
        # February 28, 2022

    def test_casino_variables(self):
        print("Testing casino variables...")
        casino_instance = Casino(2, Date("July", 4, 2023), Accountant(3000, 1000, 2000, 5))
        print(f"Game Number: {casino_instance.get_game_number()}")
        print(f"Date: {casino_instance.get_date()}")
        print(f"Accountant: {casino_instance.get_accountant()}")
        # Expected output:
        # Game Number: 2
        # Date: July 4, 2023
        # Accountant: Money In: 3000, Money Out: 1000, Total Money: 2000, Transactions: 5

    def test_accountant_variables(self):
        print("Testing Accountant variables...")
        accountant_instance = Accountant(5000, 2500, 2500, 10)
        print(f"Money In: {accountant_instance.get_money_in()}")
        print(f"Money Out: {accountant_instance.get_money_out()}")
        print(f"Total Money: {accountant_instance.get_total_money()}")
        print(f"Transaction Number: {accountant_instance.get_transaction_number()}")
        # Expected output:
        # Money In: 5000
        # Money Out: 2500
        # Total Money: 2500
        # Transaction Number: 10

    def test_random_lottery_numbers(self):
        print("Testing random lottery number generation...")
        lottery_instance = Lottery()
        lottery_instance.lotto_numbers = [randint(1, 49) for _ in range(6)]
        print(f"Generated Lottery Numbers: {lottery_instance.lotto_numbers}")
        # Expected output: A list of 6 random numbers between 1 and 49.

    def test_lottery_to_casino_transfer(self):
        print("Testing lottery to casino winnings transfer...")
        lottery_instance = Lottery(game_number=1, ticket_num=1, date=Date("December", 25, 2024))
        lottery_instance.lotto_numbers = [randint(1, 49) for _ in range(6)]
        
        print(f"Lottery Numbers: {lottery_instance.lotto_numbers}")

        # Simulate a win with a fixed amount
        winnings = 500
        casino_instance = Casino(game_number=2, date=Date("December", 26, 2024), accountant=Accountant(1000, 500, 500, 5))

        print(f"Casino Balance Before: {casino_instance.get_accountant().get_total_money()}")

        # Transfer winnings
        casino_instance.get_accountant().set_money_in(casino_instance.get_accountant().get_money_in() + winnings)

        print(f"Casino Balance After: {casino_instance.get_accountant().get_total_money()}")
        # Expected output:
        # Casino Balance Before: 500
        # Casino Balance After: 1000

    def test_combined_workflow(self):
        print("Testing combined workflow (lottery + casino)...")
        # Create lottery instance and simulate ticket purchase
        lottery_instance = Lottery(game_number=1, ticket_num=5, date=Date("January", 1, 2025))
        lottery_instance.lotto_numbers = [randint(1, 49) for _ in range(6)]

        print(f"Lottery Details: {lottery_instance}")

        # Simulate winnings and transfer to casino
        winnings = 1000
        casino_instance = Casino(game_number=2, date=Date("January", 2, 2025), accountant=Accountant(2000, 1000, 1000, 3))
        casino_instance.get_accountant().set_money_in(casino_instance.get_accountant().get_money_in() + winnings)

        print(f"Updated Casino Details: {casino_instance}")
        # Expected output:
        # Lottery Details: [Details of the lottery instance with random numbers]
        # Updated Casino Details: Casino balance updated to reflect the winnings

    def test_edge_cases(self):
        print("Testing edge cases...")

        # Edge case 1: Invalid ticket number
        try:
            Lottery(game_number=1, ticket_num=-1, date=Date("February", 29, 2024))
        except ValueError as e:
            print(f"Caught error for invalid ticket number: {e}")
        # Expected output: Error indicating invalid ticket number

        # Edge case 2: Extreme values for money in Accountant
        try:
            Accountant(money_in=-1000, money_out=500, total_money=0, transaction_number=1)
        except ValueError as e:
            print(f"Caught error for negative money in: {e}")
        # Expected output: Error indicating negative money in

        # Edge case 3: Large number of lottery tickets
        try:
            Lottery(game_number=1, ticket_num=10**6, date=Date("March", 1, 2024))
        except ValueError as e:
            print(f"Caught error for large number of tickets: {e}")
        # Expected output: Error indicating too many tickets


class LotteryTester:
    def test_to_string(self):
        print("Testing Lottery's string representation...")
        lottery_instance = Lottery()
        print(lottery_instance)
        # Expected output: Default lottery details as a string

    def test_default_constructor(self):
        print("Testing Lottery default constructor...")
        lottery_instance = Lottery()
        print(f"Game Number: {lottery_instance.game_number}")
        print(f"Ticket Number: {lottery_instance.ticket_num}")
        print(f"Date: {lottery_instance.date}")
        print(f"Lotto Numbers: {lottery_instance.lotto_numbers}")
        # Expected output: Default values for lottery instance

    def test_custom_constructor(self):
        print("Testing Lottery constructor with custom values...")
        custom_date = Date("December", 25, 2024)
        lottery_instance = Lottery(2, 10, custom_date)
        print(f"Game Number: {lottery_instance.game_number}")
        print(f"Ticket Number: {lottery_instance.ticket_num}")
        print(f"Date: {lottery_instance.date}")
        print(f"Lotto Numbers: {lottery_instance.lotto_numbers}")
        # Expected output: Custom values for lottery instance

    def test_setters(self):
        print("Testing setters for Lottery...")
        lottery_instance = Lottery()
        assert lottery_instance.set_game_number(5), "Failed to set game number"
        assert lottery_instance.set_ticket_num(50), "Failed to set ticket number"
        custom_date = Date("January", 1, 2025)
        assert lottery_instance.set_date(custom_date), "Failed to set date"
        # Expected output: No assertion errors, setters work correctly

    def test_getters(self):
        print("Testing getters for Lottery...")
        lottery_instance = Lottery(5, 50, Date("January", 1, 2025))
        print(f"Game Number: {lottery_instance.game_number}")
        print(f"Ticket Number: {lottery_instance.ticket_num}")
        print(f"Date: {lottery_instance.date}")
        # Expected output: Getter values match the input values

    def test_invalid_setters(self):
        print("Testing invalid setters for Lottery...")
        lottery_instance = Lottery()
        assert not lottery_instance.set_game_number(-1), "Invalid game number should fail"
        assert not lottery_instance.set_ticket_num(0), "Invalid ticket number should fail"
        assert not lottery_instance.set_date(None), "Invalid date should fail"
        # Expected output: No assertion errors, invalid setters fail correctly

    def test_generate_lotto_numbers(self):
        print("Testing lotto number generation...")
        lottery_instance = Lottery()
        if hasattr(lottery_instance, 'generate_lotto_numbers'):
            lottery_instance.generate_lotto_numbers()
            print(f"Lotto Numbers: {lottery_instance.lotto_numbers}")
            # Expected output: A list of generated lottery numbers
        else:
            print("The method 'generate_lotto_numbers' is not implemented yet.")
            # Expected output: Message indicating missing method


def main():
    tester = CasinoTester()
    tester.test_to_string()
    tester.test_accountant()
    tester.test_to_string_date()
    tester.test_casino_variables()
    tester.test_accountant_variables()
    tester.test_random_lottery_numbers()
    tester.test_lottery_to_casino_transfer()
    tester.test_combined_workflow()
    tester.test_edge_cases()

    lottery_tester = LotteryTester()
    lottery_tester.test_to_string()
    lottery_tester.test_default_constructor()
    lottery_tester.test_custom_constructor()
    lottery_tester.test_setters()
    lottery_tester.test_getters()
    lottery_tester.test_invalid_setters()
    lottery_tester.test_generate_lotto_numbers()

if __name__ == "__main__":
    main()
