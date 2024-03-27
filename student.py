class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)