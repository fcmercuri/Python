class Job:
    def __init__(self, name, salary, hoursWorked):
        self.name = name
        self.salary = salary
        self.hoursWorked = hoursWorked

    def print_info(self):
        print("=== Job ===")
        print(f"Name: {self.name:<10}, Salary: {self.salary:^10}, Hours Worked: {self.hoursWorked:>10}")


class Doctor(Job):
    def __init__(self, salary, hoursWorked, experience, specialty):
        # Call the parent class's constructor to handle common attributes
        super().__init__("Doctor", salary, hoursWorked)
        self.experience = experience
        self.specialty = specialty

    def print_info(self):
        # Call the parent's print method for shared attributes
        super().print_info()
        # Print the subclass-specific attributes
        print(f"Experience: {self.experience:<15} Specialty: {self.specialty:>15}")


# Create an instance of the Job class
lawyer = Job("Lawyer", "80000", "40")
lawyer.print_info()

# Create an instance of the Doctor class
doc = Doctor("120000", "50", "10 years", "Pediatrics")
doc.print_info()

