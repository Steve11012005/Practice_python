class Course:
    def __init__(self, code, title, credit_units, department, level):
        self.code = code
        self.title = title
        self.credit_units = credit_units
        self.department = department
        self.level = level
        self.students = []
        self.max_capacity = 120

    def is_full(self):
        return len(self.students) >= self.max_capacity

    def add_student(self, student):
        if not self.is_full():
            self.students.append(student)
            return True
        return False

    def __str__(self):
        return f"{self.code}: {self.title} ({self.credit_units}) units"

    def __repr__(self):
        return f" Course('{self.code}', '{self.title}','{self.credit_units}', '{self.department}', {self.level})"


class Student:
    school = "Ladoke Akintola University of Technology"

    def __init__(self, name, matric_no, department, level):
        self.name = name
        self.matric_no = matric_no
        self.department = department
        self.level = level
        self.courses = []
        self.max_credits = 24  # Maximum credits per semester

    def total_credits(self):
        return sum(course.credit_units for course in self.courses)

    def can_add_course(self, course):
        if course in self.courses:
            return False
        if self.total_credits() + course.credit_units > self.max_credits:
            return False
        if course.level > self.level:
            return False
        return True

    def register_course(self, course):
        if self.can_add_course(course):
            if course.add_student(self):
                self.courses.append(course)
                return f"Successfully registered for {course.code}"
            else:
                return f"Failed to register: {course.code} is full"
        else:
            if course in self.courses:
                return f"Failed to register: Already registered for {course.code}"
            elif self.total_credits() + course.credit_units > self.max_credits:
                return f"Failed to register: Would exceed maximum credits({self.max_credits})"
            else:
                return f"Failed to register: {course.code} is not appropriate for your level"

    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            course.students.remove(self)
            return f"Sucessfully dropped {course.code}"
        return f"Not registered for {course.code}"

    def list_courses(self):
        if not self.courses:
            return "Not registered for any courses yet"

        result = f"Courses for {self.name} ({self.matric_no}):\n"
        for course in self.courses:
            result += f"-{course}\n"
        result += f"Total credits: {self.total_credits()}/{self.max_credits}"
        return result

    def __str__(self):
        return f"{self.name} ({self.matric_no})"

    def __repr__(self):
        return f"Student('{self.name}', '{self.matric_no}', '{self.department}', '{self.level}')"


csc201 = Course("CSC201", "Computer Programming I", 3, "Computer Science", 200)
csc203 = Course("CSC203", "Discrete Structures", 2, "Computer Science", 200)
gst201 = Course("GST201", "People and Culture", 2, "General Studies", 200)
mth201 = Course("MTH201", "Mathematical Method", 3, "Mathematics", 200)
csc301 = Course("CSC301", "Data Structures", 3, "Computer Science", 300)

student = Student("Chuckwuemeka Okafor",
                  "LAUTECH/CSC/19/0421", "Computer Science", 300)

print(student.register_course(csc201))
print(student.register_course(csc203))
print(student.register_course(gst201))
print(student.register_course(mth201))
print(student.register_course(csc301))

print(student.list_courses())

print(student.drop_course(gst201))
print(student.list_courses())
