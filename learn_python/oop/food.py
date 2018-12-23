# 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe() ” method (which prints “name” and “kind” in a sentence).

"""
Instance

class Food:
    def __init__(self):
        self.name = "Carne Asada"
        self.kind = "Mexican"

    def describe(self):
        return print("Food: {}, Kind: {}".format(self.name, self.kind))


food = Food()
food.describe()
"""

# 2) Try turning describe()  from an instance method into a class and a static method. Change it back to an instance method thereafter.

"""
Class

class Food:
    name = "Carne Asada"
    kind = "Mexican"

    @classmethod
    def describe(cls):
        return print("Food: {}, Kind: {}".format(cls.name, cls.kind))


Food.describe()
"""

"""
Static

class Food:
    name = "Carne Asada"
    kind = "Mexican"

    @staticmethod
    def describe(name, kind):
        return print("Food: {}, Kind: {}".format(name, kind))


Food.describe("Ribs", "American")
"""

# 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook() ” method to “Meat” and “clean() ” to “Fruit”.


class Food:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def __repr__(self):
        return "Name: {}, Kind: {}".format(self.name, self.kind)

    def describe(self):
        return print("Food: {}, Kind: {}".format(self.name, self.kind))


class Fruit(Food):
    def __init__(self, name):
        super().__init__(name, "Fruit")

    def clean(self):
        return print("Clean Fruit with Water")


strawberry = Fruit("Strawberry")
strawberry.clean()
strawberry.describe()


class Meat(Food):
    def __init__(self, name):
        super().__init__(name, "Meat")

    def cook(self):
        return print("Cook Steak Medium")


steak = Meat("Steak")
steak.cook()
steak.describe()

# 4) Overwrite a “dunder” method to be able to print your “Food” class.

print(strawberry)
