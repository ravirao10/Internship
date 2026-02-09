class Student:
    # Class Variable (shared by all students)
    college_name = "ABC College"

    # Constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # Classmethod to change college name
    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    # Staticmethod to check pass/fail
    @staticmethod
    def is_pass(marks):
        if marks >= 35:
            return "Pass"
        else:
            return "Fail"

    # Instance method
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)
        print("-------------------")


# Creating objects
student1 = Student("Ravi", 101)
student2 = Student("Anita", 102)

# Display student details
student1.display()
student2.display()

# Change college name using classmethod
Student.change_college("XYZ Engineering College")

# Display again (college name changes for all)
student1.display()
student2.display()

# Using staticmethod
print("Student 1 Result:", Student.is_pass(78))
print("Student 2 Result:", Student.is_pass(30))
