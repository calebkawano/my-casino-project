from date import Date
import random

class Lottery:
    DEFAULT_GAME_NUM = 1
    DEFAULT_TICKET_NUM = 1
    DEFAULT_DATE = Date()

    def __init__(self, game_number=DEFAULT_GAME_NUM, ticket_num=DEFAULT_TICKET_NUM, date=DEFAULT_DATE):
        if not self.set_all(game_number, ticket_num, date):
            raise ValueError("ERROR: Problem in Lottery Full Constructor.")
        self.lotto_numbers = self.generate_lotto_numbers()
        self.user_selected = []

    def generate_lotto_numbers(self):
        #Generates a list of 6 random numbers between 1 and 49
        return random.sample(range(1, 50), 6)
    
    def user_select_lotto(self, numbers):
        #Allows user to select their lotto numbers
        if len(numbers) != 6 or not all(1 <= num <= 49 for num in numbers):
            raise ValueError("Please select exactly 6 numbers between 1 and 49.")
        self.user_selected = numbers

    def check_lotto(self):
        #Checks how many numbers the user has matched
        matches = set(self.lotto_numbers) & set(self.user_selected)
        print(f'Generated Numbers: {self.lotto_numbers}')
        print(f'Your Selected Numbers: {self.user_selected}')
        print(f'Number of Matches: {len(matches)}')
        if len(matches) > 0:
            print(f'Matching Numbers: {sorted(matches)}')
        elif len(matches) == 6:
            print('Congratulations! You have matched all 6 numbers!')
        else:
            print('No matches, better luck next time!')


    def set_game_number(self, game_number):
        if game_number >= 0:
            self.game_number = game_number
            return True
        return False

    def set_ticket_num(self, ticket_num):
        if ticket_num > 0:
            self.ticket_num = ticket_num
            return True
        return False

    def set_date(self, date):
        if date:
            self.date = date
            return True
        return False

    def set_all(self, game_number, ticket_num, date):
        return self.set_game_number(game_number) and self.set_ticket_num(ticket_num) and self.set_date(date)

    def __str__(self):
        return (
            f"Lottery Stats:\n"
            f"Game Number: {self.game_number}\n"
            f"Ticket Number: {self.ticket_num}\n"
            f"Date: {self.date}\n"
            f"Lotto Numbers: {self.lotto_numbers}"
            f"Your Numbers: {self.user_selected}"
        )

# Example Usage
if __name__ == "__main__":
    lottery = Lottery()
    print(lottery)
    #User selects their numbers
    user_numbers = [1, 2, 3, 4, 5, 6]
    lottery.user_select_lotto(user_numbers)
    #check for matches
    lottery.check_lotto()