class State:
    def __init__(self, name, capital, region, governor):
        self.name = name
        self.capital = capital
        self.region = region
        self.governor = governor
        self.local_govt_areas = []

    def add_lga(self, lga_name):
        self.local_govt_areas.append(lga_name)

    def __str__(self):
        """Human-readable representation"""
        return f"{self.name} State, Capital:{self.capital}"

    def __repr__(self):
        """Developer-friendly representation"""
        return f"State('{self.name}', '{self.capital}','{self.region}','{self.governor}')"


# Creating a state
lagos = State("Lagos", "Ikeja", "South West", "Babajide Sanwo-Olu")
lagos.add_lga("Alimosho")
lagos.add_lga("Eti-Osa")
lagos.add_lga("Surulere")

# Using string representations
print(lagos)
print(repr(lagos))
