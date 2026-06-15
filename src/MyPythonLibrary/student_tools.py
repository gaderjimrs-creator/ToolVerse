class MyStudentTools:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age):
        self.students[student_id] = {'name': name, 'age': age}

    def get_student(self, student_id):
        return self.students.get(student_id, "Student not found")

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
        else:
            return "Student not found"

    def update_student(self, student_id, name=None, age=None):
        if student_id in self.students:
            if name is not None:
                self.students[student_id]['name'] = name
            if age is not None:
                self.students[student_id]['age'] = age
        else:
            return "Student not found"
    
    def list_students(self):
        return self.students
    
    def count_students(self):
        return len(self.students)
    
    def calculate_percentage(self, student_id, marks_obtained, total_marks):
        if student_id in self.students:
            percentage = (marks_obtained / total_marks) * 100
            self.students[student_id]['percentage'] = percentage
            return percentage
        else:
            return "Student not found"
        
    def calculate_grade(self, student_id):
        if student_id in self.students:
            percentage = self.students[student_id].get('percentage', None)
            if percentage is not None:
                if percentage >= 90:
                    grade = 'A'
                elif percentage >= 80:
                    grade = 'B'
                elif percentage >= 70:
                    grade = 'C'
                elif percentage >= 60:
                    grade = 'D'
                else:
                    grade = 'F'
                self.students[student_id]['grade'] = grade
                return grade
            else:
                return "Percentage not calculated for this student"
        else:
            return "Student not found"
    
    def calculate_cgpa(self, student_id, grades):
        if student_id in self.students:
            grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
            total_points = sum(grade_points.get(grade, 0) for grade in grades)
            gpa = total_points / len(grades)
            self.students[student_id]['gpa'] = gpa
            return gpa
        else:
            return "Student not found"
    
    def get_student_report(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            report = f"Student ID: {student_id}\n"
            report += f"Name: {student['name']}\n"
            report += f"Age: {student['age']}\n"
            report += f"Percentage: {student.get('percentage', 'Not calculated')}\n"
            report += f"Grade: {student.get('grade', 'Not calculated')}\n"
            report += f"GPA: {student.get('gpa', 'Not calculated')}\n"
            return report
        else:
            return "Student not found"
    
    def get_all_students_report(self):
        report = ""
        for student_id, student in self.students.items():
            report += f"Student ID: {student_id}\n"
            report += f"Name: {student['name']}\n"
            report += f"Age: {student['age']}\n"
            report += f"Percentage: {student.get('percentage', 'Not calculated')}\n"
            report += f"Grade: {student.get('grade', 'Not calculated')}\n"
            report += f"GPA: {student.get('gpa', 'Not calculated')}\n"
            report += "-------------------------\n"
        return report
    
    def get_top_student(self):
        top_student_id = None
        top_percentage = -1
        for student_id, student in self.students.items():
            percentage = student.get('percentage', None)
            if percentage is not None and percentage > top_percentage:
                top_percentage = percentage
                top_student_id = student_id
        if top_student_id is not None:
            return self.get_student_report(top_student_id)
        else:
            return "No students with calculated percentage"
    
    def get_bottom_student(self):
        bottom_student_id = None
        bottom_percentage = float('inf')
        for student_id, student in self.students.items():
            percentage = student.get('percentage', None)
            if percentage is not None and percentage < bottom_percentage:
                bottom_percentage = percentage
                bottom_student_id = student_id
        if bottom_student_id is not None:
            return self.get_student_report(bottom_student_id)
        else:
            return "No students with calculated percentage"
    
    def get_average_percentage(self):
        total_percentage = 0
        count = 0
        for student in self.students.values():
            percentage = student.get('percentage', None)
            if percentage is not None:
                total_percentage += percentage
                count += 1
        if count > 0:
            return total_percentage / count
        else:
            return "No students with calculated percentage"
    
    def get_average_gpa(self):
        total_gpa = 0
        count = 0
        for student in self.students.values():
            gpa = student.get('gpa', None)
            if gpa is not None:
                total_gpa += gpa
                count += 1
        if count > 0:
            return total_gpa / count
        else:
            return "No students with calculated GPA"
    
    def get_students_with_grade(self, grade):
        students_with_grade = []
        for student_id, student in self.students.items():
            if student.get('grade', None) == grade:
                students_with_grade.append(student_id)
        return students_with_grade
    
    def get_students_above_percentage(self, percentage):
        students_above = []
        for student_id, student in self.students.items():
            student_percentage = student.get('percentage', None)
            if student_percentage is not None and student_percentage > percentage:
                students_above.append(student_id)
        return students_above
    
    def get_students_below_percentage(self, percentage):
        students_below = []
        for student_id, student in self.students.items():
            student_percentage = student.get('percentage', None)
            if student_percentage is not None and student_percentage < percentage:
                students_below.append(student_id)
        return students_below
