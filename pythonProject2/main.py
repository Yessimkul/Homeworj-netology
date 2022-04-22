class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lr(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def aver_st(self):
        sum_ = 0
        for k, v in self.grades.items():
            sum_ += (sum(v) / len(v))
        return sum_ / len(self.grades)

    def __str__(self):
        some_student = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.aver_st()} \n' \
                       f'Курсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}'
        return some_student

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student')
            return
        return self.aver_st() < other.aver_st()


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

    def aver_lr(self):
        sum_ = 0
        for k, v in self.grades.items():
            sum_ += (sum(v) / len(v))
        return sum_ / len(self.grades)

    def __str__(self):
        some_lecturer = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.aver_lr()}'
        return some_lecturer

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer')
            return
        return self.aver_lr() < other.aver_lr()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f'Имя: {self.name} \nФамилия: {self.surname}'
        return some_reviewer


best_student = Student('Yessimkul', 'Kereikulov', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

second_student = Student('Ruoy', 'Eman', 'male')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Git']
second_student.finished_courses += ['Введение в программирование']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']

second_lecturer = Lecturer('Once', 'Told me')
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Git']

best_student.rate_lr(cool_lecturer, 'Python', 10)
best_student.rate_lr(cool_lecturer, 'Python', 10)
best_student.rate_lr(cool_lecturer, 'Python', 9)
best_student.rate_lr(cool_lecturer, 'Git', 9)
best_student.rate_lr(cool_lecturer, 'Git', 8)
best_student.rate_lr(cool_lecturer, 'Git', 8)

best_student.rate_lr(second_lecturer, 'Python', 9)
best_student.rate_lr(second_lecturer, 'Python', 9)
best_student.rate_lr(second_lecturer, 'Python', 10)
best_student.rate_lr(second_lecturer, 'Git', 8)
best_student.rate_lr(second_lecturer, 'Git', 10)
best_student.rate_lr(second_lecturer, 'Git', 8)

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Git', 8)
cool_reviewer.rate_hw(best_student, 'Git', 7)
cool_reviewer.rate_hw(best_student, 'Git', 10)

cool_reviewer.rate_hw(second_student, 'Python', 10)
cool_reviewer.rate_hw(second_student, 'Python', 7)
cool_reviewer.rate_hw(second_student, 'Python', 10)
cool_reviewer.rate_hw(second_student, 'Git', 10)
cool_reviewer.rate_hw(second_student, 'Git', 9)
cool_reviewer.rate_hw(second_student, 'Git', 7)

# print(cool_lecturer.grades)

students_dict = {best_student: best_student.grades,
                second_student: second_student.grades}

lecturer_dict = {cool_lecturer: cool_lecturer.grades,
                 second_lecturer: second_lecturer.grades}

def average_st(dict):
    for k, v in dict.items():
        print(k)
        for sub, gr_list in v.items():
            print(f'Cредняя оценка за курс {sub}: {sum(gr_list)/len(gr_list)}')

# average_st(students_dict)


def average_lr(dict):
    for k, v in dict.items():
        print(k)
        for sub, gr_list in v.items():
            print(f'Cредняя оценка за курс {sub}: {sum(gr_list) / len(gr_list)}')

average_lr(lecturer_dict)


# print(best_student)
# print(cool_lecturer.courses_attached)
# print(cool_reviewer)
# print(cool_lecturer < second_lecturer)
# print(best_student < second_student)
