class vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def sue(self):
        print("Bus name is:",self.name)
        print("max speed is:",self.max_speed)
        print("mileage is:",self.mileage)

class bus(vehicle):
    def __init__(self,name, max_speed, mileage):
        super().__init__(name,max_speed, mileage)
    

c1 = bus("Volvo",60,16)
c1.sue()