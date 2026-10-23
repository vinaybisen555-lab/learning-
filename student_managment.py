
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def update_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            return True
        return False

    def display(self):
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.__marks)
        print("------------------------")


class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self):
        roll_no = input("Enter roll number: ")

        if any(s.roll_no == roll_no for s in self.students):
            print("Roll number already exists!")
            return

        name = input("Enter student name: ")

        try:
            marks = float(input("Enter marks (0-100): "))
            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100.")
                return
        except ValueError:
            print("Please enter valid marks.")
            return

        student = Student(roll_no, name, marks)
        self.students.append(student)
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No student records found.")
            return

        for student in self.students:
            student.display()

    def search_student(self):
        roll_no = input("Enter roll number to search: ")

        for student in self.students:
            if student.roll_no == roll_no:
                student.display()
                return

        print("Student not found.")

    def update_marks(self):
        roll_no = input("Enter roll number: ")

        for student in self.students:
            if student.roll_no == roll_no:
                try:
                    marks = float(input("Enter new marks: "))
                    if student.update_marks(marks):
                        print("Marks updated successfully!")
                    else:
                        print("Marks must be between 0 and 100.")
                except ValueError:
                    print("Please enter valid marks.")
                return

        print("Student not found.")

    def run(self):
        while True:
            print("\n===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student")
            print("4. Update Marks")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.update_marks()
            elif choice == "5":
                print("Exiting Student Management System.")
                break
            else:
                print("Invalid choice. Try again.")


app = StudentManagement()
app.run()
