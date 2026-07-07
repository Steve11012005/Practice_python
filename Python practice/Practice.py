class Student:
    school = "Ladoke Akintola university of Technology"

    def __init__(self, name, matric_number, department):
        self.name = name
        self.matric_number = matric_number
        self.department = department
        self.courses = []
        self.grades = {}

    def add_course(self, course_code, course_title, credit_units):
        course = {
            "code": course_code,
            "title": course_title,
            "units": credit_units
        }
        self.courses.append(course)

    def add_grade(self, course_code, score):
        if score >= 70:
            grade = 'A'
        elif score >= 60:
            grade = 'B'
        elif score >= 50:
            grade = 'C'
        elif score >= 45:
            grade = 'D'
        elif score >= 40:
            grade = 'E'
        else:
            grade = 'F'
        self.grades[course_code] = {
            "score": score,
            "grade": grade
        }


student1 = Student("Farinto Stephen",
                   "LCSC2023/23/5016", "Computer Science")
student1.add_course("CSC310", "Numerical Computation", 3)
student1.add_course("MTH203", "Linear Algebra", 2)
student1.add_grade("CSC310", 90)
student1.add_grade("MTH203", 90)

print(f"Student Name: {student1.name}")
print(f"Department: {student1.department}")
print(f"School: {Student.school}")
