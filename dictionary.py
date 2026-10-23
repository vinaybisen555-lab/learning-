
students = {
    101: {"name": "vinay", "marks": 85},
    102: {"name": "abc", "marks": 92},
    103: {"name": "Rahul", "marks": 78}
}

student_id = int(input("Enter Student ID: "))

if student_id in students:
    print("Name:", students[student_id]["name"])
    print("Marks:", students[student_id]["marks"])
else:
    print("Student not found")
