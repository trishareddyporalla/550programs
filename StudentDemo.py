class StudentInformationSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, roll_no, unit_tests):
        self.students[roll_no] = {'name': name, 'unit_tests': unit_tests}

    def update_unit_tests(self, roll_no, unit_tests):
        if roll_no in self.students:
            self.students[roll_no]['unit_tests'] = unit_tests
        else:
            print("Student not found!")
            

    def get_student_info(self, roll_no):
        if roll_no in self.students:
            return self.students[roll_no]
        else:
            print("Student not found!")
            return None

    def print_all_students_info(self):
        print("Student Information:")
        for roll_no, student_info in self.students.items():
            print(f"Roll No: {roll_no}, Name: {student_info['name']}, Unit Tests: {student_info['unit_tests']}")


# Example usage:
sis = StudentInformationSystem()

sis.add_student("pradeep", 101, [85, 90, 88, 92])
sis.add_student("Amgoth", 102, [78, 85, 80, 88])

sis.print_all_students_info()

sis.update_unit_tests(501, [90, 92, 88, 94])
sis.update_unit_tests(503, [80, 82, 85, 90])

sis.print_all_students_info()
