from classTeacher import Teacher
from test_classTeacher.conftest import Teacher


def test_teacher_init(teacher):
    assert len(Teacher.teacher_dict) == 1
    assert Teacher.teacher_dict == {'test_name':['test_education', 'test_experience']}

def test_get_name(teacher):
    assert teacher.get_name() == 'test_name'

def test_get_education(teacher):
    assert teacher.get_education() == 'test_education'

def test_get_experience(teacher):
    assert teacher.get_experience() == 'test_experience'

def test_set_experience(teacher):
    assert teacher.set_experience('4') == 'Опыт работы увеличен на 4'

def test_add_mark(teacher):
    assert teacher.add_mark("test_student", 4) == "test_name поставил оценку 4 студенту test_student"

def test_remove_mark(teacher):
    assert teacher.remove_mark("test_student", 4) == 'test_name удалил оценку 4 студенту test_student'

def test_give_a_consultation(teacher):
    assert teacher.give_a_consultation('test_university_class') == 'test_name провел консультацию в классе test_university_class'

def test_fire_teacher(teacher):
    assert teacher.fire_teacher() == "test_name был уволен!"
    assert teacher.fire_teacher() == "test_name уже уволили!"
    assert len(Teacher.teacher_dict) == 0





