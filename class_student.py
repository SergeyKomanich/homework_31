class Student:
    grades = []

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = []

    def add_grade(self, grade: int):
        self.grades.append(grade)

    def total_grade(self):
        sum_grade = 0
        count = 0
        if len(self.grades) > 1:
            for grade in self.grades:
                sum_grade += grade
                count += 1
        return sum_grade


class Group:
    group_list = []

    def __int__(self):
        self.group_list = []

    def student_add(self, student: Student):
        self.group_list.append(student)

    def student_remove(self, student: Student):
        self.group_list.remove(student)

    def print_lst_student(self):
        if len(self.group_list) > 0:
            for stud in self.group_list:
                print('{:20}'.format(' '.join([stud.name, stud.surname])), end='')
                if len(stud.grades) > 0:
                    for grade in stud.grades:
                        print('{:^3}'.format(grade), end=' ')
                    print("sumGrade:"'{:5}'.format(stud.total_grade()), end='\n')
                else:
                    print('У этого студента оценок пока нет', end='\n')
        else:
            print('Журнал  студентов пуст.')
        print('\n')


student1 = Student('Serhii', 'Komanich')
student2 = Student('Igor', 'Petrov')
student3 = Student('Viktor', 'Shevchenko')
student4 = Student('Lubov', 'Ivanova')
gruop = Group()
gruop.student_add(student1)
gruop.student_add(student2)
gruop.student_add(student3)
gruop.student_add(student4)
student1.add_grade(10)
student1.add_grade(10)
student1.add_grade(9)

student2.add_grade(9)
student2.add_grade(9)
student2.add_grade(10)

student3.add_grade(10)
student3.add_grade(7)
student3.add_grade(8)

# student4.add_grade(9)
# student4.add_grade(10)
# student4.add_grade(8)

gruop.print_lst_student()
