
class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def display(self):
        self.display_name()
        print("Roll Number:", self.roll_no)


s1 = Student("Vinay", 101)
s1.display()
