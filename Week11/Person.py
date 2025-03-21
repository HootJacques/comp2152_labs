class Person:
    def __init__(self, p_name, p_age, p_height):
        print("Constructing Person Object")
        self.__name = p_name
        self.__age = p_age
        self.__height = p_height
        self.public__prop = "I'm a public property"

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __del__(self):
        print("Deleting Person Object with Garbage Collector")


person1 = Person("Mike", 57, 187)

print(f"Person Name: {person1.name}")
person1.name = "Name Override"
print(f"Person Name: {person1.name}")
#print(f"Test: {person1.public__prop}")