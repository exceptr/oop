class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        grades_list = []
        for i in self.grades.values():
            grades_list.extend(i)
        avg_grade = sum(grades_list) / len(grades_list)
        return round(avg_grade, 2)

    def courses_finished(self):
        courses = ", ".join(self.finished_courses)
        return courses

    def courses_progress(self):
        courses = ", ".join(self.courses_in_progress)
        return courses

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grade() < other.average_grade()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {self.courses_progress()}\nЗавершенные курсы: {self.courses_finished()}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def average_grade(self):
        grades_list = []
        for i in self.grades.values():
            grades_list.extend(i)
        avg_grade = sum(grades_list) / len(grades_list)
        return round(avg_grade, 2)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_grade() < other.average_grade()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['Введение в программирование']
best_student.finished_courses += ['Git']

best_student1 = Student('Robot', 'Kava', 'your_gender')
best_student1.courses_in_progress += ['Java']
best_student1.courses_in_progress += ['Python']
best_student1.finished_courses += ['Английский для программистов']
best_student1.finished_courses += ['Git']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor1 = Reviewer('Mad', 'Max')
cool_mentor1.courses_attached += ['Java']

cool_lecturer = Lecturer('Aboba', 'Alba')
cool_lecturer.courses_attached += ['PHP']

cool_lecturer1 = Lecturer('Derji', 'Dverb')
cool_lecturer1.courses_attached += ['1C']
cool_lecturer1.courses_attached += ['C#']
# cool_lecturer1.courses_attached += ['PHP']

cool_reviewer = Reviewer('Alex', 'Bolt')

cool_mentor1.rate_hw(best_student1, 'Java', 8)
cool_mentor1.rate_hw(best_student1, 'Java', 10)
cool_mentor1.rate_hw(best_student1, 'Java', 9)

cool_mentor1.rate_hw(best_student, 'Java', 7)
cool_mentor1.rate_hw(best_student, 'Java', 7)
cool_mentor1.rate_hw(best_student, 'Java', 10)

cool_mentor.rate_hw(best_student1, 'Python', 8)
cool_mentor.rate_hw(best_student1, 'Python', 9)
cool_mentor.rate_hw(best_student1, 'Python', 5)

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 8)
cool_mentor.rate_hw(best_student, 'Python', 10)

best_student.rate_lecturer(cool_lecturer, 'PHP', 10)
best_student.rate_lecturer(cool_lecturer, 'PHP', 3)
best_student.rate_lecturer(cool_lecturer, 'PHP', 7)

best_student.rate_lecturer(cool_lecturer1, 'C#', 10)
best_student.rate_lecturer(cool_lecturer1, 'C#', 8)
best_student.rate_lecturer(cool_lecturer1, 'C#', 4)

# print(best_student.grades)
# print(best_student1.grades)
print(cool_lecturer.grades)
print(cool_lecturer1.grades)
# print(cool_reviewer)
# print(cool_lecturer)
# print(best_student)
# print(best_student1)
# print(cool_lecturer > cool_lecturer1)
# print(best_student > best_student1)

student_list = [best_student, best_student1]
lecturer_list = [cool_lecturer, cool_lecturer1]


def avg_rate_students_course(students=student_list):
    grades_list = []
    for student in students:
        for grades in student.grades['Python']:
            grades_list.append(grades)
    avg_grade = sum(grades_list) / len(grades_list)
    return round(avg_grade, 2)


# print(avg_rate_students_course())


def avg_rate_lecturer_course(lecturers=lecturer_list):
    grades_list = []
    for lecturer in lecturers:
        for grades in lecturer.grades['C#']:
            grades_list.append(grades)
    avg_grade = sum(grades_list) / len(grades_list)
    return round(avg_grade, 2)
print(avg_rate_lecturer_course())