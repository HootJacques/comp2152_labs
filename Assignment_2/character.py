import random

class Character:
    def __init__(self):
        print("Initializing Character")
        self.__combat_strength = random.randint(1,6)
        self.__health_points = random.randint(1,10)

    def __del__(self):
        print("Deleting Character")

    @property
    def combat_strength(self):
        return self.__combat_strength
    @combat_strength.setter
    def combat_strength(self, value):
        self.__combat_strength = value

    @property
    def health_points(self):
        return self.__health_points
    @health_points.setter
    def health_points(self, value):
        self.__health_points = value