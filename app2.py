from flask import Flask, render_template,redirect,url_for,request
students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Error reading file")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")


""" 
##print(name)
def varargs(name,**double_args):
    print(name)
    print(double_args["subject"],double_args["verb"], double_args["adjective"])
"""

# student id will be overriden,call exactly with
# the attributes
# add_student(name ="Mark",student_id=15)
# varargs("Mark",subject = "Python", verb = "is", adjective = "good")
read_file()
print_students_titlecase()
student_name = input("Student name")
student_id = input("Student id")
add_student(student_name, student_id)
save_file(student_name)
# function nesting -> possible
