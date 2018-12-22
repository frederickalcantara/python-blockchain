class Car():
    # top_speed = 160
    # warnings = []
    def __init__(self, starting_top_speed=160):
        self.top_speed = starting_top_speed
        self.warnings = []

    def __repr__(self):
        print('Printing...')
        return 'Top Speed: {}, Warnings: {}'.format(self.top_speed, self.warnings)

    def drive(self):
        print('I am driving not certainly faster than {}'.format(self.top_speed))


car1 = Car()
car1.drive()

# Car.top_speed = 200
car1.warnings.append('New Warning')
# print(car1.__dict__)
print(car1)

car2 = Car(200)
car2.drive()

car3 = Car(250)
car3.drive()


# __init__ is a constructor in python
# Have to return self in any method for an object
