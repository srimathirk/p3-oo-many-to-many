from datetime import datetime

class Student:

    all = []

    def __init__(self, name):
        self.name = name
        Student.all.append(self)

    def enroll_in_course(self, course):
        Enrollment(self, course)

    def enrollments(self):
        return [enrollment for enrollment in Enrollment.all if enrollment.student == self]

    def courses(self):
        return [enrollment.course for enrollment in self.enrollments()]

class Course:

    all = []

    def __init__(self, title):
        self.title = title
        Course.all.append(self)

    def enrollments(self):
        return [enrollment for enrollment in Enrollment.all if enrollment.course == self]

    def students(self):
        return [enrollment.student for enrollment in self.enrollments()]

    def enroll_student(self, student):
        Enrollment(student, self)

class Enrollment:

    all = []

    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.enrollment_date = datetime.now()
        Enrollment.all.append(self)

student = Student('Steve')
course = Course('Math 31')

student.enroll_in_course(course)
print(student.enrollments()[0].enrollment_date)

print(course.enrollments()[0].enrollment_date)

print(student.enrollments()[0].course.title)


