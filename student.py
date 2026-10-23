
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)


s1 = Student("Vinay", 101, 85)
s1.display()
