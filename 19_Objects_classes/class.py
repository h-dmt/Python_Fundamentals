class Class:
    __students_count = 22

    def __init__(self, name: str):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        average = sum(self.grades)/len(self.grades)
        return round(average, 2)

    def __repr__(self):
        out_average = self.get_average_grade()
        return f"The students in {self.name}: {', '.join(self.students)}." \
               f" Average grade: {out_average}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("Kiro", 2.00)
a_class.add_student("Rick", 4.5)
a_class.add_student("Gianni", 3.50)
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
a_class.get_average_grade()
print(a_class)
