class Vehicle:
    def __init__(self,type,capicity):
        self.type = type
        self.capicity = capicity
    def fare(self):
        return 100*self.capicity
class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        bus_fare = base_fare + 0.1*base_fare
        return bus_fare
bus = Bus("school bus ",30)
print(bus.fare())
       