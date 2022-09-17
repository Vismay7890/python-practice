class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.color = "white"
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass
    # def __init__(self, name, max_speed, mileage):
    #     super().__init__(name, max_speed, mileage)


c1 = Bus("Volvo",220,19)
print(c1.color)