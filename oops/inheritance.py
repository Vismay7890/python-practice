class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def seating_capacity(self,capacity):
        return f"The seating capacity of a {self.name} is {capacity}"
class Bus(Vehicle):
    def seating_capacity(self, capacity = 65):
        return super().seating_capacity(capacity = 65)


c1 = Bus("Passenger Volvo",220,19)
print(c1.seating_capacity())
