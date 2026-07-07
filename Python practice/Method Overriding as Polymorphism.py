# We've already seen method overriding in the inheriatnce section. Let's explore how it enables polymorphism in an educational context:
class AcademicPerson:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def role(self):
        return "Academic Person"

    def describe_responsibilities(self):
        return "Has academic responsibilities"


class Lecturer(AcademicPerson):
    def __init__(self, name, id_number, department, courses):
        super().__init__(name, id_number)
        self.department = department
        self.courses = courses

    def role(self):
        return "Lecturer"

    def describe_responsibilities(self):
        return f"Teaches{','. join(self.courses)} in the {self.department} department"


class Student(AcademicPerson):
    def __init__(self, name, id_number, department, level):
        super().__init__(name, id_number)
        self.department = department
        self.level = level

    def role(self):
        return "Student"

    def describe_responsibilities(self):
        return f"Studies in {self.department} department at {self.level} level"


class ResearchAssistant(AcademicPerson):
    def __init__(self, name, id_number, research_area, supervisor):
        super().__init__(name, id_number)
        self.research_area = research_area
        self.supervisor = supervisor

    def role(self):
        return "Research Assistant"

    def describe_responsibilities(self):
        return f"Assists {self.supervisor} with research in {self.research_area}"
# Function that demonstrates polymorphism


def print_academic_info(academic_person):
    print(f"Name: {academic_person.name}")
    print(f"ID: {academic_person.id_number}")
    print(f"Role: {academic_person.role()}")
    print(f"Responsibilities: {academic_person.describe_responsibilities()}")
    print("-" * 40)


# Create different types of academic persons
people = [
    Lecturer("Dr. Adebayo Johnson", "LEC/2020/042",
             "Computer Science", ["Programming", "Algorithms"]),
    Student("Chioma Okonkwo", "CSC/2023/001", "Computer Science", 200),
    ResearchAssistant("Ibrahim Musa", "RA/2022/007",
                      "Artificial Intelligence", "Prof. Oluwaseun Adeyemi")
]
# Process all academic persons polymorphically
for person in people:
    print_academic_info(person)
