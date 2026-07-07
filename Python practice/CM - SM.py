class NairaBill:
    denominations = [5, 10, 20, 50, 100, 200, 500, 1000]
    currency_code = "NGN"

    def __init__(self, value):
        if value in self.denominations:
            self.value = value
        else:
            raise ValueError(f"{value} is not a Naira denomination")

    def get_description(self):
        return f"{self.value} Naira bill"

    @classmethod
    def get_highest_denomination(cls):
        return max(cls.denominations)

    @classmethod
    def add_new_denomination(cls, value):
        if value not in cls.denominations:
            cls.denominations.append(value)
            cls.denominations.sort()
            return f"Added {value} to available denominations"
        return f"{value} is already a valid denomination"

    @staticmethod
    def convert_to_kobo(naira_amount):
        return naira_amount*100

    @staticmethod
    def is_valid_currency_code(code):
        return code == "NGN"


# Using the instance method
bill = NairaBill(500)
print(bill.get_description())

# Using class methods
print(f"Highest denomination: {NairaBill.get_highest_denomination()}")
print(NairaBill.add_new_denomination(2000))
print(f"Updated highest denomination: {NairaBill.get_highest_denomination()}")

# Using static methods
print(f"500 Naira in kobo:{NairaBill.convert_to_kobo(500)}")
print(f"Is NGN a valid code? {NairaBill.is_valid_currency_code('NGN')}")
print(f"Is USD a valid code? {NairaBill.is_valid_currency_code('USD')}")
