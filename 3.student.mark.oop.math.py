import math
import numpy as np
import curses

class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__marks = {}

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def add_mark(self, course_id, mark):
        mark = math.floor(mark * 10) / 10  # Round down to 1 decimal digit
        self.__marks[course_id] = mark

    def get_marks(self):
        return self.__marks

    def calculate_gpa(self, credits):
        marks = np.array(list(self.__marks.values()))
        weighted_marks = marks * credits
        gpa = np.sum(weighted_marks) / np.sum(credits)
        return round(gpa, 2)  # Round to 2 decimal digits

    def __str__(self):
        return f"ID: {self.__id}, Name: {self.__name}, DoB: {self.__dob}, Marks: {self.__marks}"


class Course:
    def __init__(self, id, name, credits):
        self.__id = id
        self.__name = name
        self.__credits = credits

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits

    def __str__(self):
        return f"ID: {self.__id}, Name: {self.__name}, Credits: {self.__credits}"


class StudentCourseManager:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def input_number_of_students(self):
        return int(input("Number of students: "))

    def input_student_information(self):
        id = input("id: ")
        name = input("name: ")
        dob = input("Date of Birth (year-month-birth): ")
        while len(dob) != 10 or dob[4] != '-' or dob[7] != '-':
            print("Please enter again")
            dob = input("Date of Birth (year-month-birth): ")
        return Student(id, name, dob)

    def input_number_of_courses(self):
        return int(input("Number of courses: "))

    def input_course_information(self):
        id = int(input("course ID: "))
        name = input("course name: ")
        credits = float(input("credits: "))
        return Course(id, name, credits)

    def input_marks(self):
        student_id = input("Select student id: ")
        for student in self.__students:
            if student.get_id() == student_id:
                self.list_courses()
                course_id = int(input("Select a course id: "))
                for course in self.__courses:
                    if course.get_id() == course_id:
                        mark = float(input("Mark: "))
                        mark = math.floor(mark * 10) / 10  
                        while mark > 10 or mark < 0:
                            print("Please enter again: ")
                            mark = float(input("Mark: "))
                            mark = math.floor(mark * 10) / 10
                        student.add_mark(course_id, mark)
                        print("Success")
                    else:
                        print("Please recheck your course id")
                        return course_id
            else:
                print("Please recheck your id")
                return student_id

    def list_courses(self):
        print("List of Courses:")
        for course in self.__courses:
            print(course)

    def list_students(self):
        print("List of Students:")
        for student in self.__students:
            print(student)

    def sort_students_by_gpa(self):
        self.__students.sort(key=lambda x: x.calculate_gpa([course.get_credits() for course in self.__courses]), reverse=True)

    def run(self):
        num_students = self.input_number_of_students()
        for _ in range(num_students):
            self.__students.append(self.input_student_information())

        num_courses = self.input_number_of_courses()
        for _ in range(num_courses):
            self.__courses.append(self.input_course_information())

        self.input_marks()

        self.list_students()
        self.list_courses()

        self.sort_students_by_gpa()
        print("Students sorted by GPA:")
        self.list_students()


def display_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Press 'q' to quit")
    stdscr.refresh()

curses.wrapper(display_menu)

manager = StudentCourseManager()
manager.run()
