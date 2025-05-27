# Parent Class
class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")


# Subclass: Student
class Student(Person):
    def __init__(self, name, gender, student_number,course):
        super().__init__(name, gender)
        self.student_number = student_number
        self.course =course

    def display_info(self):
        super().display_info()
        print(f"Student Number: {self.student_number}")
        print(f"Course assigned: {self.course}")


# Subclass: Lecturer
class Lecturer(Person):
    def __init__(self, name, gender, staff_number, duty_type):
        super().__init__(name, gender)
        self.staff_number = staff_number
        self.duty_type = duty_type

    def display_info(self):
        super().display_info()
        print(f"Staff Number: {self.staff_number}")
        print(f"Duty Type: {self.duty_type}")


# Subclass: SupportStaff
class SupportStaff(Person):
    def __init__(self, name, gender, staff_number, duty_type):
        super().__init__(name, gender)
        self.staff_number = staff_number
        self.duty_type = duty_type

    def display_info(self):
        super().display_info()
        print(f"Staff Number: {self.staff_number}")
        print(f"Duty Type: {self.duty_type}")


# Created Objects and Display the respective Information
stu = Student("Alvin Aine", "M", "2300705288","Sciences in Software Engineering")
lect = Lecturer("Dr. James Muwanika", "M", "LECT0025", "Teach Numerical Analysis")
staff = SupportStaff("Martha Kyisa", "F", "STF0121", "Library Assistant")

print("=== Student Info ===")
stu.display_info()

print("\n=== Lecturer Info ===")
lect.display_info()

print("\n=== Support Staff Info ===")
staff.display_info()
