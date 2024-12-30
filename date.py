class Date:
    DEFAULT_MONTH = "January"
    DEFAULT_DAY = 1
    DEFAULT_YEAR = 2000

    def __init__(self, month=DEFAULT_MONTH, day=DEFAULT_DAY, year=DEFAULT_YEAR):
        if not self.set_all(month, day, year):
            raise ValueError("ERROR: Bad data in Date Full Constructor!")

    def set_month(self, month):
        if self.is_valid_month(month):
            self.month = month
            return True
        return False

    def set_day(self, day):
        if self.is_valid_day(day):
            self.day = day
            return True
        return False

    def set_year(self, year):
        if self.is_valid_year(year):
            self.year = year
            return True
        return False

    def set_all(self, month, day, year):
        return self.set_month(month) and self.set_day(day) and self.set_year(year)

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def get_year(self):
        return self.year

    def __str__(self):
        return f"{self.month} {self.day}, {self.year}"

    def equals(self, other):
        if not isinstance(other, Date):
            return False
        return self.month == other.month and self.day == other.day and self.year == other.year

    def precedes(self, other):
        if not isinstance(other, Date):
            return False
        return (
            self.year < other.year or
            (self.year == other.year and self.month_to_int(self.month) < self.month_to_int(other.month)) or
            (self.year == other.year and self.month == other.month and self.day < other.day)
        )

    @staticmethod
    def is_valid_month(month):
        return month in Date.month_to_int_map()

    @staticmethod
    def is_valid_day(day):
        return 1 <= day <= 31

    @staticmethod
    def is_valid_year(year):
        return 1000 <= year <= 9999

    @staticmethod
    def month_to_int(month):
        return Date.month_to_int_map().get(month, 0)

    @staticmethod
    def month_to_int_map():
        return {
            "January": 1, "February": 2, "March": 3, "April": 4, "May": 5,
            "June": 6, "July": 7, "August": 8, "September": 9, "October": 10,
            "November": 11, "December": 12
        }

    @staticmethod
    def int_to_month(month):
        int_to_month_map = {v: k for k, v in Date.month_to_int_map().items()}
        return int_to_month_map.get(month, None)


# Example Usage
if __name__ == "__main__":
    try:
        default_date = Date()
        print(default_date)

        custom_date = Date("February", 14, 2024)
        print(custom_date)

        print(custom_date.precedes(default_date))
    except ValueError as e:
        print(e)
