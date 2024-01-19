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
        self.__marks[course_id] = mark

    def get_marks(self):
        return self.__marks

    def __str__(self):
        return f"ID: {self.__id}, Name: {self.__name}, DoB: {self.__dob}, Marks: {self.__marks}"


class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"ID: {self.__id}, Name: {self.__name}"


class StudentCourseManager:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def input_number_of_students(self):
        return int(input("Number of students: "))

    def input_student_information(self):
        id = input("id: ")
        name = input("name: ")
        dob = int(input("Date of Birth (year-month-birth): "))
        while dob > 20240101 or dob < 19140101:
            print("Please enter again")
            dob = int(input("Date of Birth (year-month-birth): "))
        return Student(id, name, dob)

    def input_number_of_courses(self):
        return int(input("Number of courses: "))

    def input_course_information(self):
        id = int(input("course ID: "))
        name = input("course name: ")
        return Course(id, name)

    def input_marks(self):
        student_id = input("Select student id: ")
        for student in self.__students:
            if student.get_id() == student_id:
                self.list_courses()
                course_id = int(input("Select a course id: "))
                for course in self.__courses:
                    if course.get_id() == course_id:
                        mark = int(input("Mark: "))
                        while mark > 10 or mark < 0:
                            print("Please enter again: ")
                            mark = int(input("Mark: "))
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


manager = StudentCourseManager()
manager.run()
