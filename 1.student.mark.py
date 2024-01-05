# Initialize empty lists to store students and courses
students = []
courses = []

def input_student_info():
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
    return (id, name, dob, {})

def input_course_info():
    id = input("Enter course ID: ")
    name = input("Enter course name: ")
    return (id, name)

def input_marks():
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    mark = input("Enter mark for the student: ")
    for student in students:
        if student[0] == student_id:
            student[3][course_id] = mark
            print("Mark added successfully.")
            return
    print("Student not found.")

def list_students():
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

def list_courses():
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def show_student_marks():
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    for student in students:
        if student[0] == student_id:
            mark = student[3].get(course_id)
            if mark is not None:
                print(f"Student ID: {student_id}, Course ID: {course_id}, Mark: {mark}")
                return
            else:
                print("No mark found for this student and course.")
                return
    print("Student not found.")

num_students = int(input("Enter number of students: "))
for _ in range(num_students):
    students.append(input_student_info())

num_courses = int(input("Enter number of courses: "))
for _ in range(num_courses):
    courses.append(input_course_info())

input_marks()

print("\nList of students:")
list_students()

print("\nList of courses:")
list_courses()

show_student_marks()
