students = []


class Student:
    school_name = "Gymnasium"

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    # override = _str_

    def __str__(self):
        return "Student"+" "+self.name

    def get_name_capitalise(self):
        return self.name.capitalize()

    def get_school_name(self):
        self.school_name

# student = Student()
# student.add_student("Mark")


class HighSchoolStudent(Student):

    school_name = "Other school"

    def get_school_name(self):
        return "This is a high school student"


    def get_name_capitalise(self):
        original_value = super().get_name_capitalise()
        return original_value + "-HS"


james = HighSchoolStudent("Hello!")
print(james.get_name_capitalise())
