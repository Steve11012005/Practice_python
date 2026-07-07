class University:
    country = "Nigeria"
    educational_system = "6-3-3-4"
    governing_body = "NUC"

    def __init__(self, name, location, founding_year):
        self.name = name
        self.location = location
        self.founding_year = founding_year
        self.faculties = []

    def add_faculty(self, faculty_name):
        self.faculties.append(faculty_name)

    @classmethod
    def get_governing_body(cls):
        return cls.governing_body

    # Creating university objetcs
# pyright: ignore[reportUndefinedVariable]
unilag = University("University of Lagos", "Lagos", 1962)
oau = University("Obafemi Awolowo University", "Ile-Ife", 1961)

# Accessing instance variables
print(f"{unilag.name} was founded in {unilag.founding_year}")
print(f"{oau.name} is located in {oau.location}")

# Acessing class variables
print(f"Both universities are in {University.country}")
print(f"They are governed by the {University.get_governing_body()}")

# Modifying instance variables
unilag.add_faculty("Faculty of Engineering")
oau.add_faculty("Faculty of Science")

print(f"{unilag.name} has {len(unilag.faculties)} faculty")
print(f"{oau.name} has {len(oau.faculties)} faculty")

# Modifying a class variable affects all instances
University.governing_body = "National Universities Commission"
print(f"Updated governing body: {unilag.governing_body}")
print(f"Same for all universities: {oau.governing_body}")
