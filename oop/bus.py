from vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, starting_top_speed=160):
        super().__init__(starting_top_speed)
        self.passengers = []

    def add_group(self, passengers):
        self.passengers.extend(passengers)


bus1 = Bus(150)
bus1.add_group(['Fred', 'freddyal'])
print(bus1.passengers)
bus1.drive()

# Use super() to call attributes from the parent constructor of the base Class
