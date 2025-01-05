class Teacher:
    teacher_dict = {}

    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience
        Teacher.teacher_dict[self.__name] = [self.__education, self.__experience]


    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        self.__experience += experience
        return f'Опыт работы увеличен на {experience}'

    def add_mark(self, student, grade):
        return f'{self.__name} поставил оценку {grade} студенту {student}'

    def remove_mark(self, student, grade):
        return f'{self.__name} удалил оценку {grade} студенту {student}'

    def give_a_consultation(self, university_class):
        return f'{self.__name} провел консультацию в классе {university_class}'

    def fire_teacher(self):
        if self.__name in Teacher.teacher_dict.keys():
            Teacher.teacher_dict.pop(self.__name)
            return f'{self.__name} был уволен!'
        else:
            return f'{self.__name} уже уволили!'














