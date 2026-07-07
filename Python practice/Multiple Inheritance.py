class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old"


class Teacher:
    def __init__(self, subjects, salary):
        self.subjects = subjects
        self.salary = salary

    def teach(self):
        subjects_list = ",".join(self.subjects)
        return f"I can teach {subjects_list}."

    def get_salary(self):
        return f"My salary is #{self.salary} per annum."


class Principal(SchoolMember, Teacher):
    def __init__(self, name, age, subjects, salary, school_name):
        SchoolMember.__init__(self, name, age)
        Teacher.__init__(self, subjects, salary)
        self.school_name = school_name

    def manage_school(self):
        return f"I manage {self.school_name}."

    def full_introduction(self):
        intro = self.introduce()
        teaching = self.teach()
        salary = self.get_salary()
        management = self.manage_school()
        return f"{intro}{teaching}{salary}{management}"


principal = Principal(
    "Mrs. Folashade Adeniran",
    45,
    ["Mathematics", "Physics"],
    3000000,
    "Sunshine Secondary School, Abuja"
)
print(principal.introduce())
print(principal.teach())
print(principal.manage_school())
print("\nFull introduction:")
print(principal.full_introduction())
print("\nMethof Resolution Order for Principal class:")
print(Principal.__mro__)
