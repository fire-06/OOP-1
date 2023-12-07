class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def calculate_avg_grade(self):
        if not self.grades:
            return 0.0

        total_grades = 0
        total_count = 0

        for course, grades in self.grades.items():
            total_grades += sum(grades)
            total_count += len(grades)

        return round(total_grades / total_count, 1) if total_count > 0 else 0.0

    def __lt__(self, other):
        return self.calculate_avg_grade() < other.calculate_avg_grade()



    def __str__(self):
        avg_grade = self.calculate_avg_grade()
        in_progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)

        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {avg_grade}\n" \
               f"Курсы в процессе изучения: {in_progress}\n" \
               f"Завершенные курсы: {finished}"

def avg_grade_for_course(students, course_name):
    total_grades = 0
    total_students = 0

    for student in students:
        if course_name in student.grades:
            total_grades += sum(student.grades[course_name])
            total_students += len(student.grades[course_name])

    return round(total_grades / total_students, 2) if total_students > 0 else 0.0
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def calculate_avg_grade(self):
        if not self.grades:
            return 0.0

        total_grades = 0
        total_count = 0

        for course, grades in self.grades.items():
            total_grades += sum(grades)
            total_count += len(grades)

        return round(total_grades / total_count, 1) if total_count > 0 else 0.0

    def __lt__(self, other):
        return self.calculate_avg_grade() < other.calculate_avg_grade()


    def __str__(self):
        avg_grade = self.calculate_avg_grade()
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {avg_grade}"

def avg_lecture_grade(lecturers, course_name):
    total_grades = 0
    total_lecturers = 0

    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course_name in lecturer.grades:
            total_grades += sum(lecturer.grades[course_name])
            total_lecturers += len(lecturer.grades[course_name])

    return round(total_grades / total_lecturers, 2) if total_lecturers > 0 else 0.0


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}"

some_student = Student('Ruoy', 'Eman', 'male')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

some_student_2 = Student('Rusy', 'Alice', 'male')
some_student_2.courses_in_progress += ['Python', 'Git']
some_student_2.finished_courses += ['Введение в программирование']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_lecturer_2 = Lecturer('Anton', 'Babby')
some_lecturer_2.courses_attached += ['Python']

some_reviewer = Reviewer('John', 'Doe')
some_reviewer.courses_attached += ['Python']

some_reviewer_2 = Reviewer('Another', 'Batty')
some_reviewer_2.courses_attached += ['Python']

some_student.add_grade(some_lecturer, 'Python', 10)
some_student.add_grade(some_lecturer, 'Python', 9)
some_student.add_grade(some_lecturer, 'Python', 10)

some_student_2.add_grade(some_lecturer_2, 'Python', 10)
some_student_2.add_grade(some_lecturer_2, 'Python', 9)
some_student_2.add_grade(some_lecturer_2, 'Python', 9)

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 8)

some_reviewer_2.rate_hw(some_student_2, 'Python', 10)
some_reviewer_2.rate_hw(some_student_2, 'Python', 9)
some_reviewer_2.rate_hw(some_student_2, 'Python', 10)

print(some_student)
print()
print(some_student_2)
print()
print(some_lecturer_2)
print()
print(some_lecturer)
print()
print(some_reviewer_2)
print()
print(some_reviewer)
print()
if some_lecturer < some_student:
    print("Средняя оценка за лекции у some_lecturer меньше, чем средняя оценка за домашние задания у some_student")
else:
    print("Средняя оценка за лекции у some_lecturer больше или равна, чем средняя оценка за домашние задания у some_student")

if some_lecturer_2 < some_student_2:
    print("Средняя оценка за лекции у some_lecturer меньше, чем средняя оценка за домашние задания у some_student")
else:
    print(
            "Средняя оценка за лекции у some_lecturer больше или равна, чем средняя оценка за домашние задания у some_student")

print()

students_list = [some_student, some_student_2]
lecturers_list = [some_lecturer, some_lecturer_2]

course_name = 'Python'
avg_student_grade = avg_grade_for_course(students_list, course_name)
avg_lecturer_grade = avg_lecture_grade(lecturers_list, course_name)

print(f"Средняя оценка за домашние задания по курсу {course_name}: {avg_student_grade}")
print()
print(f"Средняя оценка за лекции по курсу {course_name}: {avg_lecturer_grade}")

