from student import Student
from teacher import Teacher

students = []
teachers = []

def add_student(name, age, course):
    student = Student(name, age, course)
    students.append(student)

def add_teacher(name, teacher_id, subject):
    teacher = Teacher(name, teacher_id, subject)
    teachers.append(teacher)

def display_all_students():
    print("***** Student List *****")
    for student in students:
        student.display_info()
        print()

def display_all_teachers():
    print("***** Teacher List *****")
    for teacher in teachers:
        teacher.display_info()
        print()


add_student("Ayşe", 25, "Math")
add_student("Gonca", 25, "Physics")
add_student("Gülsüm", 29, "Chemical")

add_teacher("Nur", 100, "Math")
add_teacher("Mete", 101, "Physics")

display_all_students()
print()
display_all_teachers()
