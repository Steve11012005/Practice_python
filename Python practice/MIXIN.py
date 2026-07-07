class GradingMixin:
    def calculate_grade(self, score):
        if score >= 70:
            return 'A'
        elif score >= 60:
            return 'B'
        elif score >= 50:
            return 'C'
        elif score >= 45:
            return 'D'
        elif score >= 40:
            return 'E'
        else:
            return 'F'

    def get_grade_point(self, grade):
        grade_points = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
        return grade_points.get(grade, 0)


class ReportMixin:
    def generate_report_card(self, results):
        report = "SEMESTER REPORT CARD\n"
        report += "=" * 40 + "\n"

        total_points = 0
        total_units = 0

        for course, data in results.items():
            score = data['score']
            units = data['units']
            grade = self.calculate_grade(score)
            points = self.get_grade_point(grade) * units

            total_points += points
            total_units += units

            report += f"{course} ({units} units): {score} - {grade}\n"
        if total_units > 0:
            gpa = total_points / total_units
            report += "=" * 40 + "\n"
            report += f"GPA:{gpa:.2f}\n"

        return report


class AcademicAdvisor(GradingMixin, ReportMixin):
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def advise_student(self, student_name, results):
        report = self.generate_report_card(results)
        return f"Academic Advisor: {self.name}\nStudent: {student_name}\n\n{report}"


# Create an academic advisor
advisor = AcademicAdvisor("Dr. Chukwu Nneka", "computer Science")

# Student results
results = {
    'CSC201': {'score': 72, 'units': 3},
    'MTH201': {'score': 65, 'units': 3},
    'GEG203': {'score': 58, 'units': 2},
    'GST201': {'score': 82, 'units': 2},
    'PHY205': {'score': 45, 'units': 1}
}
# Generate student report
print(advisor.advise_student("Adebayo Oluwaseun", results))
