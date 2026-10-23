with open("students.txt", "w") as file:
    file.write("101,Amit,85\n")
    file.write("102,Riya,92\n")

print("Student records saved successfully.")

with open("students.txt", "r") as file:
    print("\nStudent Records:")
    print(file.read())
