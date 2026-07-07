class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def calculate_monthly_salary(self):
        return self.salary/12

    def get_details(self):
        return f"Name: {self.name}, ID: {self.employee_id}, Annual Salary: #{self.salary}"


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department, bonus_percentage=10):
        super().__init__(name, employee_id, salary)
        self.department = department
        self.bonus_percentage = bonus_percentage

    def calculate_monthly_salary(self):
        base_salary = super().calculate_monthly_salary()
        bonus = {self.bonus_percentage / 100} * base_salary
        return base_salary + bonus

    def get_details(self):
        basic_details = super().get_details()
        return f"{basic_details}, Department: {self.department}, Bonus: {self.bonus_percentage}%"


manager = Manager("Olabisi Ayeni", "M001", 6000000,
                  "Information Technology", 15)

print(manager.get_details)
print(f"Monthly salary: #{manager.calculate_monthly_salary():.2f}")
