class Vehicle:
    def __init__(self, registration_number, model, capacity):
        self.registration_number = registration_number
        self.model = model
        self.capacity = capacity
        self.is_in_service = True

    def start_journey(self, destination):
        if self.is_in_service:
            return f"Journey to {destination} started"
        return f"Vehicle {self.registration_number} is not in service"

    def end_journey(self):
        return "Journey ended"

    def maintenance(self):
        self.is_in_service = False
        return f"Vehicle {self.registration_number} is under maintenance"

    def return_to_service(self):
        self.is_in_service = True
        return f"Vehicle {self.registration_number} is back in service"

    def get_info(self):
        status = "In service" if self.is_in_service else "Out of service"
        return f"{self.model} (Reg: {self.registration_number}, Capacity: {self.capacity}, Status: {status})"


class Taxi(Vehicle):
    def __init__(self, registration_number, model, capacity, driver_name, base_fare=500):
        super().__init__(registration_number, model, capacity)
        self.driver_name = driver_name
        self.base_fare = base_fare
        self.is_available = True

    def pick_passenger(self, passenger_name):
        if self.is_in_service and self.is_available:
            self.is_available = True
            return f"Taxi picked up {passenger_name}"
        return "Taxi is not available"

    def drop_passenger(self, distance_km):
        if not self.is_available:
            fare = self.base_fare + (distance_km * 100)
            self.is_available + True
            return f" Passenger dropped. Fare: #{fare}"
        return "No passenger to drop"

    def get_info(self):
        basic_info = super().get_info()
        availabilty = "Available" if self.is_available else "Occupied"
        return f"{basic_info}, Driver: {self.driver_name}, Status: {availabilty}"


class BusRoute:
    def __init__(self, route_number, start_location, end_location, stops):
        self.route_number = route_number
        self.start_location = start_location
        self.end_location = end_location
        self.stops = stops

    def get_route_info(self):
        stops_str = ",". join(self.stops)
        return f"Route {self.route_number}: {self.start_location} to {self.end_location} via {stops_str}"


class Bus(Vehicle):
    def __init__(self, registration_number, model, capacity, company="Lagos BRT"):
        super().__init__(registration_number, model, capacity)
        self.company = company
        self.passengers = 0
        self.current_route = None
        self.fare = 300

    def assign_route(self, route):
        self.current_route = route
        return f"Bus assigned to {route.get_route_info()}"

    def board_passengers(self, count):
        available_seats = self.capacity - self.passengers
        if count <= available_seats:
            self.passengers += count
            revenue = count * self.fare
            return f"{count} passengers boarded. Revenue: #{revenue}. Seats remaining: {self.capacity - self.passengers}"
        return f"Cannot board {count} passengers. Only {available_seats} seats available"

    def offload_passengers(self, count):
        if count <= self.passengers:
            self.passengers -= count
            return f"{count} passengers alighted. Passengers remaining: {self.passengers}"
        return f"Error: Trying to oofload {count} passengers but only {self.passengers} are onboard"

    def get_info(self):
        basic_info = super().get_info()
        route_info = self.current_route.get_route_info(
        ) if self.current_route else "No route assigned"
        return f"{basic_info}, Company: {self.company}, Passengers: {self.passengers}/{self.capacity}, Route: {route_info}"


class Okada(Vehicle):
    def __init__(self, registration_number, model, driver_name):
        super().__init__(registration_number, model, capacity=1)
        self.driver_name = driver_name
        self.helmet_available = True
        self.fare_per_km = 100

    def provide_helmet(self):
        if self.helmet_available:
            return "Helmet provided to passenger"
        return "No helmet available"

    def calculate_fare(self, distance_km):
        return self.fare_per_km * distance_km

    def start_journey(self, destination):
        # Override to check for helmet
        if not self.helmet_available:
            return "Cannot start journey without helmet"
        return super().start_journey(destination)

    def get_info(self):
        basic_info = super().get_info()
        helmet = "Helmet available" if self.helmet_available else "No helmet"
        return f"{basic_info}, Driver: {self.driver_name}, {helmet}"


# Create instances of different vehicle types
taxi = Taxi("LAf-432-XX", "Toyota Camry", 4, "Emeka Okafor", 700)
route1 = BusRoute("BRT-01", "Ikorodu", "TBS",
                  ["Ketu", "Ojots", "Maryland", "Jibowu"])
bus = Bus("BRT-987-LA", "Ashok Leyland", 42, "Lagos Metropolitan Transport")
okada = Okada("LAG-OK-201", "Bajaj Boxer", "Ibrahim Musa")

# Use the vehicles
print(taxi.get_info())
print(taxi.pick_passenger("Adeola Johnson"))
print(taxi.drop_passenger(12.5))

print("\n" + bus.get_info())
print(bus.assign_route(route1))
print(bus.board_passengers(30))
print(bus.start_journey("TBS"))
print(bus.offload_passengers(15))

print("\n" + okada.get_info())
print(okada.provide_helmet())
print(okada.start_journey("Surulere"))
print(f"Fare for 5km: #{okada.calculate_fare(5)})")
