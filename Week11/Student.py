from Person import Person

class Student(Person):
    def __init__(self, p_name, p_age, p_height, p_major):
        super().__init__(p_name, p_age, p_height)
        self.major = p_major
        print(f"Constructing Student Object")


student1 = Student("Kyle", 26, 160, "Programming")
print(f"Student name is: {student1.name}")
print(f"Student major is: {student1.major}")