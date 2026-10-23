
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")


s1 = Student("Vinay", 80)

print("Name:", s1.name)
print("Marks:", s1.get_marks())

s1.set_marks(90)
print("Updated Marks:", s1.get_marks())
