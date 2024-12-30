class Accountant:
    def __init__(self, money_in=0, money_out=0, total_money=0, transaction_number=0):
        self.money_in = money_in
        self.money_out = money_out
        self.total_money = total_money
        self.transaction_number = transaction_number
        if not self.set_all(money_in, money_out, total_money, transaction_number):
            raise ValueError("Invalid initial Accountant parameters")

    # Setters / Mutators
    def set_money_in(self, money_in):
        if money_in >= 0:
            self.money_in = money_in
            self.update_total_money()
            return True
        else:
            print("ERROR: Negative Money In")
            return False

    def set_money_out(self, money_out):
        if money_out <= self.money_in:
            self.money_out = money_out
            self.update_total_money()
            return True
        else:
            print("ERROR: Money Out Exceeds Money In")
            return False

    def update_total_money(self):
        self.total_money = self.money_in - self.money_out
        if self.total_money >= 0:
            return True
        else:
            print("ERROR: Total Money is Negative")
            return False

    def set_transaction_number(self, transaction_number):
        if transaction_number >= 0:
            self.transaction_number = transaction_number
            return True
        else:
            print("ERROR: Transaction Number Must Be Non-Negative")
            return False

    def set_all(self, money_in, money_out, total_money, transaction_number):
        return (self.set_money_in(money_in) and
                self.set_money_out(money_out) and
                self.update_total_money() and
                self.set_transaction_number(transaction_number))

    # Getters / Accessors
    def get_money_in(self):
        return self.money_in

    def get_money_out(self):
        return self.money_out

    def get_total_money(self):
        return self.total_money

    def get_transaction_number(self):
        return self.transaction_number

    # String Representation
    def __str__(self):
        return (f"Money In: {self.money_in}, Money Out: {self.money_out}, "
                f"Total Money: {self.total_money}, Transactions: {self.transaction_number}")
