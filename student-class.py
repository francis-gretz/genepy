class Student:
    def __init__(self, name: str):
        self.name = name
        self.grades = []

    def add_exam(self, grade: float):
        self.grades.append(grade)

    def get_mean(self):
        sum = 0
        for grade in self.grades:
            if grade == 0:
                return 0
            else:
                sum += grade

        return sum / len(self.grades)


class School:
    def __init__(self, name: str):
        self.name = name
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def get_mean(self):
        sum = 0
        for student in self.students:
            grade = student.get_mean()

            if grade == 0:
                return 0
            else:
                sum += grade

        return sum / len(self.students)

    def get_best_student(self):
        max = -99999

        for student in self.students:
            grade = student.get_mean()

            if max < grade:
                max = grade
                best_student = student

        return best_student


class City:
    def __init__(self, name: str):
        self.name = name
        self.schools = []

    def add_school(self, school: School):
        self.schools.append(school)

    def get_mean(self):
        sum = 0
        for school in self.schools:
            grade = school.get_mean()

            if grade == 0:
                return 0
            else:
                sum += grade

        return sum / len(self.schools)

    def get_best_school(self):
        max = -99999

        for school in self.schools:
            grade = school.get_mean()

            if max < grade:
                max = grade
                best_school = school

        return best_school

    def get_best_student(self):
        max = -99999

        for school in self.schools:
            best_student_school = school.get_best_student()
            grade = best_student_school.get_mean()

            if max < grade:
                max = grade
                best_student = best_student_school

        return best_student


# paris = City("paris")
# hkis = School("hkis")
# paris.add_school(hkis)
# for student_name, student_grades in (
#     ("alice", (1, 2, 3)),
#     ("bob", (2, 3, 4)),
#     ("catherine", (3, 4, 5)),
#     ("daniel", (4, 5, 6)),
# ):
#     student = Student(student_name)
#     for grade in student_grades:
#         student.add_exam(grade)
#     hkis.add_student(student)
# print(paris.get_best_school().name)
# print(paris.get_best_student().name)
