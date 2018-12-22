from vehicle import Vehicle


class Car(Vehicle):
    # top_speed = 160
    # warnings = []

    def brag(self):
        print('Check out my car')


car1 = Car()
car1.drive()

# Car.top_speed = 200
car1.add_warning('New Warning')
# car1.__warnings.append([])
# print(car1.__dict__)
print(car1)

car2 = Car(200)
car2.drive()
print(car2.get_warnings())

car3 = Car(250)
car3.drive()
print(car3.get_warnings())


# __init__ is a constructor in python
# Have to return self in any method for an object
# Add __ in front of a attribute to indicate that this is private in a constructor
