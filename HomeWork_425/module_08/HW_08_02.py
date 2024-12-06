class Teacher:

    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience


    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        self.__experience += experience
        return f'Опыт работы увеличен на {experience}'

    def get_teacher_data(self):
        if self.__experience < 5:
            return f'{self.__name} образование {self.__education}, опыт работы {self.__experience} года'
        else:
            return f'{self.__name} образование {self.__education}, опыт работы {self.__experience} лет'

    def add_mark(self, student, grade):
        return f'{self.__name} поставил оценку {grade} студенту {student}'

    def remove_mark(self, student, grade):
        return f'{self.__name} удалил оценку {grade} студенту {student}'

    def give_a_consultation(self, university_class):
        return f'{self.__name} провел консультацию в классе {university_class}'

teacher_1 = Teacher('Иван Петрович', 'БГПУ', 4)
print(teacher_1.get_teacher_data())
print(teacher_1.set_experience(2))
print(teacher_1.get_teacher_data())
print(teacher_1.add_mark('Петр Сидоров', 4))
print(teacher_1.remove_mark('Дмитрий Степанов', 3))
print(teacher_1.give_a_consultation('9Б'))
print()
print("Задание 2")
print()

"""Задание 2"""


class DisciplineTeacher(Teacher):

    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self.__discipline = discipline
        self.__job_title = job_title

    def get_discipline(self):
        return self.__discipline

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, job_title):
        self.__job_title = job_title
        return f'Новая должность: {job_title}'

    def get_teacher_data(self):
        new_teacher_data = super().get_teacher_data()
        return f'{new_teacher_data}. \nПредмет: {self.__discipline}, должность: {self.__job_title}'

    def add_mark(self, student, grade):
        new_add_mark = super().add_mark(student, grade)

        return f'{new_add_mark}. \nПредмет: {self.__discipline}'

    def remove_mark(self, student, grade):
        new_remove_mark = super().remove_mark(student, grade)
        return f'{new_remove_mark}. \nПредмет: {self.__discipline}'

    def give_a_consultation(self, university_class):
        new_give_a_consultation = super().give_a_consultation(university_class)
        return f'{new_give_a_consultation} \nпо предмету {self.__discipline} как {self.__job_title}'


teacher_2 = DisciplineTeacher('Иван Петрович', 'БГПУ', 4, "Химия", 'профессор')

print(teacher_2.get_teacher_data())
print()
print(teacher_2.set_job_title('Директо'))
print()
print(teacher_2.get_teacher_data())
print()
print(teacher_2.add_mark('Петр Сидоров', 4))
print()
print(teacher_2.remove_mark('Дмитрий Степанов', 3))
print()
print(teacher_2.give_a_consultation('9Б'))













