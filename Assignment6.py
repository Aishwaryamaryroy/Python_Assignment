# Exercise 1
# class Course:
#     def __init__(self, course_code, course_name, credit_hours):
#         self.course_code = course_code
#         self.course_name = course_name
#         self.credit_hours = credit_hours
#
#     def display_info(self):
#         print(f"Course Code: {self.course_code}")
#         print(f"Course Name: {self.course_name}")
#         print(f"Credit Hours: {self.credit_hours}")
#
# class CoreCourse(Course):
#     def __init__(self, course_code, course_name, credit_hours, required_for_major):
#         Course.__init__(self, course_code, course_name, credit_hours)
#         self.required_for_major = required_for_major
#
#     def display_info(self):
#         Course.display_info(self)
#         print(f"Required for Major: {'Yes' if self.required_for_major else 'No'}")
#
# class ElectiveCourse(Course):
#     def __init__(self, course_code, course_name, credit_hours, elective_type):
#         Course.__init__(self, course_code, course_name, credit_hours)
#         self.elective_type = elective_type
#
#     def display_info(self):
#         Course.display_info(self)
#         print(f"Elective Type: {self.elective_type}")
#
# course1 = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
# course2 = ElectiveCourse("MATH201", "Calculus II", 4, "technical")
#
# print("Core Course Info:")
# course1.display_info()
#
# print("\nElective Course Info:")
# course2.display_info()

#Exercise 2
from employee import Employee
employee1 = Employee("John Doe", 50000)

print("Employee Name:", employee1.get_name())
print("Employee Salary:", employee1.get_salary())

