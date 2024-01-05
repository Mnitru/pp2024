students = []
courses = []

def input_number_of_students():
    return int(input("Number of students: "))

def input_student_information():
    id = input("id: ")
    name = input("name: ")
    dob = int(input("Date of Birth (YYYY-MM-DD): "))
    while dob > 20240101 or dob < 19140101 :
            print("Please enter again")
            dob = int(input("Date of Birth (YYYY-MM-DD): "))
    return (id, name, dob, {})

def input_number_of_courses():
    return int(input("number of courses: "))

def input_course_information():
    id = input("course ID: ")
    name = input("course name: ")
    return (id, name)

def input_marks(students, courses):
    list_students(students)
    student_id = input("Select a student ID: ")
    list_courses(courses)
    course_id = input("Select a course ID: ")
    mark = int(input("Enter mark for the student: "))
    while mark > 10 or mark < 0:
        print("please enter again:")
        mark = int(input("Enter mark for the student: "))
    for student in students:
        if student[0] == student_id:
            student[3][course_id] = mark
            print("successfully.")
            return
    print("Student not found.")

def list_courses(courses):
    print("List of Courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def list_students(students):
    print("List of Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")    

num_students = input_number_of_students()
for _ in range(num_students):
    students.append(input_student_information())

num_courses = input_number_of_courses()
for _ in range(num_courses):
    courses.append(input_course_information())

input_marks(students, courses)

list_students(students)

list_courses(courses)

