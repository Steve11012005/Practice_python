class TraditionalMarket:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def describe(self):
        return f"{self.name} is a traditional market loacted in {self.location}"

    def calculate_stall_fee(self, size_sqm):
        # Traditional markets charge based on size
        base_fee = 5000  # Naira
        return base_fee * size_sqm


class ShoppingMall:
    def __init__(self, name, location, air_conditioned=True):
        self.name = name
        self.location = location
        self.air_conditioned = air_conditioned

    def describe(self):
        ac_status = "an air-conditioned" if self.air_conditioned else "a"
        return f"{self.name} is {ac_status} shopping mall is located in {self.location}"

    def calculate_stall_fee(self, size_sqm):
        # Malls charge premium rates
        base_fee = 15000  # Naira
        ac_premium = 5000 if self.air_conditioned else 0
        return (base_fee + ac_premium) * size_sqm


class OnlineMarketplace:
    def __init__(self, name, website):
        self.name = name
        self.website = website

    def describe(self):
        return f"{self.name} is an online marketplace accessible at {self.website}"

    def calculate_stall_fee(self, size_sqm):
        # Online marketplaces don't care about physical size, they charge a flat fee
        return 50000  # Naira
# Function that uses duck typing


def display_market_info(market, stall_size=10):
    print(market.describe())
    fee = market.calculate_stall_fee(stall_size)
    print(f"Stall fee for {stall_size} sqm: #{fee:,}")
    print("-" * 40)


# Create diiferent types of markets
markets = [
    TraditionalMarket("Oyingbo Market", "Lagos Mainland"),
    ShoppingMall("Ikeja City Mall", "Ikeja,Lagos"),
    OnlineMarketplace("Jumia", "www.jumia.com.ng")
]
# Process all markets using duck typing
for market in markets:
    display_market_info(market)
