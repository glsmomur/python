class Teacher:
    def __init__(self, name, teacher_id, subject):
        self.name = name
        self.teacher_id = teacher_id
        self.subject = subject

    def display_info(self):
        print("Teacher Name:", self.name)
        print("Teacher ID:", self.teacher_id)
        print("Subject:", self.subject)