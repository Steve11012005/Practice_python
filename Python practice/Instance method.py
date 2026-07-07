class MobileSubscription:
    def __init__(self, phone_number, network_provider, plan="Pay As You Go"):
        self.phone_number = phone_number
        self.network_provider = network_provider
        self.plan = plan
        self.data_balance = 0  # in MB
        self.airtime_balance = 0  # in Naira

    def recharge(self, amount):
        self.airtime_balance += amount
        print(
            f"Successfully recharged #{amount}. New balance: #{self.airtime_balance}")

    def buy_data(self, amount, data_volume):
        if self.airtime_balance >= amount:
            self.airtime_balance -= amount
            self.data_balance += data_volume
            print(f"Successfully purchased {data_volume}MB for #{amount}")
            print(f"New data balance: {self.data_balance}MB")
            print(f"Remaining airtime:#{self.airtime_balance}")
        else:
            print(
                f"Insufficient balance. You need #{amount}but have #{self.airtime_balance}")

    def make_call(self, duration_seconds, rate_per_second=1.5):
        cost = duration_seconds * rate_per_second
        if self.airtime_balance >= cost:
            self.airtime_balance -= cost
            print(f"Call completed ({duration_seconds} seconds)")
            print(f"Cost: #{cost}")
            print(f"Remaining airtime:#{self.airtime_balance}")
        else:
            print(
                f"Insufficient balance for this call. Cost: #{cost}, Balance: #{self.airtime_balance}")

    def check_balance(self):
        print(f"Phone Number: {self.phone_number}")
        print(f"Network: {self.network_provider}")
        print(f"Plan: {self.plan}")
        print(f"Airtime Balance: #{self.airtime_balance}")
        print(f"Data Balance: {self.data_balance}MB")


# Creating a subscription
my_phone = MobileSubscription("09136064353", "MTN")
# Using Methods
my_phone.recharge(1000)
my_phone.buy_data(500, 1024)  # Buy 1GB data
my_phone.make_call(600)  # 600-second call
my_phone.check_balance()
