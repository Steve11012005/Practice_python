class UniversityMember:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        self.university = "Ladoke Akintola University of Technology"

    def display_info(self):
        return f"Name:{self.name}, ID:{self.id_number}, University:{self.university}"

    def get_id_card(self):
        return f"{self.university} ID Card - {self.id_number}"


class Student(UniversityMember):
    def __init__(self, name, id_number, department, level):
        # Initilaize parent class attributes
        super().__init__(name, id_number)
        # Add child class attributes
        self.department = department
        self.level = level

    def display_info(self):
        # Override the parent method to include student-specific info
        basic_info = super().display_info()
        return f"{basic_info}, Department: {self.department}, Level:{self.level}"


# Create a student
student = Student("Ngozi Okonkwo", "STU/2023/0042", "Computer Science", 300)
# Access inherited method
print(student.get_id_card())
# Access overridden method
print(student.display_info())
