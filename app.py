
students = {}


def add_student(student_id, name, marks):
    if student_id in students:
        raise ValueError("Student ID already exists")

    if not name.strip():
        raise ValueError("Student name cannot be empty")

    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100")

    students[student_id] = {
        "name": name,
        "marks": marks
    }

    return students[student_id]


def get_student(student_id):
    if student_id not in students:
        raise ValueError("Student not found")

    return students[student_id]


def calculate_grade(marks):
    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100")

    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"


if __name__ == "__main__":
    add_student(101, "Ravi", 85)
    student = get_student(101)

    print("Student Management System")
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    print("Grade:", calculate_grade(student["marks"]))
