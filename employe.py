class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


e1 = Employee("Rahul", 201, 30000)
e1.display()
