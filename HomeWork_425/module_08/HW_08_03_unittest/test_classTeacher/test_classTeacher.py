import unittest
from classTeacher import Teacher

class TestTeacher(unittest.TestCase):
    teacher = Teacher('test_name', 'test_education', 'test_experience')

    def test_1_init(self):
        self.assertEqual(len(Teacher.teacher_dict), 1)
        self.assertEqual(Teacher.teacher_dict, {'test_name': ['test_education', 'test_experience']})

    def test_2_get_name(self):
        self.assertEqual(self.teacher.get_name(), 'test_name')

    def test_3_get_education(self):
        self.assertEqual(self.teacher.get_education(), 'test_education')

    def test_4_get_experience(self):
        self.assertEqual(self.teacher.get_experience(), 'test_experience')

    def test_5_set_experience(self):
        self.assertEqual(self.teacher.set_experience("4"), 'Опыт работы увеличен на 4')

    def test_6_add_mark(self):
        self.assertEqual(self.teacher.add_mark('test_student', 3), "test_name поставил оценку 3 студенту test_student")

    def test_7_remove_mark(self):
        self.assertEqual(self.teacher.remove_mark('test_student', 3), "test_name удалил оценку 3 студенту test_student")

    def test_8_give_a_consultation(self):
        self.assertEqual(self.teacher.give_a_consultation("test_university_class"), "test_name провел консультацию в классе test_university_class")

    def test_9_fire_teacher(self):
        self.assertEqual(self.teacher.fire_teacher(), 'test_name был уволен!')
        self.assertEqual(self.teacher.fire_teacher(), 'test_name уже уволили!')
        self.assertEqual(Teacher.teacher_dict, {})

